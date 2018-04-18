from django.shortcuts import render,redirect
from django.http import *
from shop.models import Order,Product,Dealer,Employee
from shop.forms import OrderForm,ProductForm,DealerForm,EmployeeForm
from shop.utils import render_to_pdf
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    employees=Employee.objects.all()
    orders=Order.objects.all()
    return render(request,'shop/search.html',{'orders':orders,'employees':employees})

@login_required
def dealers(request):
    dealers=Dealer.objects.all()
    return render(request,'shop/dealers.html',{'dealers':dealers})

@login_required
def dealerproducts(request,id):
    dealer=Dealer.objects.get(id=id)
    products=dealer.product_set.all()
    return render(request,'shop/products.html',{'products':products})

@login_required
def dealeradd(request):
    if request.method=='POST':
        form=DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dealers')
    else:
        form=DealerForm()
    return render(request,'shop/dealeradd.html',{'form':form})

@login_required
def dealerdetail(request,id):
    dealer=Dealer.objects.get(id=id)
    return render(request,'shop/dealerdetail.html',{'dealer':dealer})

@login_required
def dealeredit(request,id):
    dealer=Dealer.objects.get(id=id)
    return render(request,'shop/dealeredit.html',{'dealer':dealer})

@login_required
def dealerupdate(request,id):
    if request.method=='POST':
        dealer=Dealer.objects.get(id=id)
        dealer.name=request.POST['name']
        dealer.contact=request.POST['contact']
        dealer.address=request.POST['address']
        dealer.website=request.POST['website']
        dealer.save()
        return HttpResponseRedirect('/dealers')

@login_required
def dealerdelete(request,id):
    Dealer.objects.get(id=id).delete()
    return HttpResponseRedirect('/dealers')

@login_required
def products(request):
    products=Product.objects.all()
    return render(request,'shop/products.html',{'products':products})

@login_required
def productdetail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'shop/productdetail.html',{'product':product})

@login_required
def productadd(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form=ProductForm()
    return render(request,'shop/productadd.html',{'form':form})

@login_required
def productedit(request,id):
    product=Product.objects.get(id=id)
    return render(request,'shop/productedit.html',{'product':product})

@login_required
def productupdate(request,id):
    if request.method=='POST':
        product=Product.objects.get(id=id)
        product.productid=request.POST.get('productid','None')
        product.name=request.POST['name']
        product.description=request.POST['description']
        product.price=request.POST['price']
        product.stock=request.POST['stock']
        
        product.save()
        return HttpResponseRedirect('/products')

@login_required
def productdelete(request,id):
    Product.objects.get(id=id).delete()
    return HttpResponseRedirect('/products')

@login_required
def orders(request):
    orders=Order.objects.all()
    return render(request,'shop/orders.html',{'orders':orders})

@login_required
def orderdetail(request,id):
    order=Order.objects.get(id=id)
    return render(request,'shop/orderdetail.html',{'order':order})

@login_required
def orderadd(request):
    products=Product.objects.all()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders')
    else:
        form=OrderForm()
    return render(request,'shop/orderadd.html',{'form':form,'products':products})

@login_required
def orderedit(request,id):
    order=Order.objects.get(id=id)
    return render(request,'shop/orderedit.html',{'order':order})

@login_required
def orderupdate(request,id):
    if request.method=='POST':
        order=Order.objects.get(id=id)
        order.orderid=request.POST['orderid']
        order.name=request.POST['name']
        order.contact=request.POST['contact']
        order.address=request.POST['address']
        order.orderby=request.POST['orderby']
        order.delivery_date=request.POST['delivery_date']
        order.status=request.POST['status']
        order.paymentmode=request.POST['paymentmode']
        order.save()
        return HttpResponseRedirect('/orders')

@login_required
def orderdelete(request,id):
    Order.objects.get(id=id).delete()
    return HttpResponseRedirect('/orders')

@login_required
def employees(request):
    employees=Employee.objects.all()
    return render(request,'shop/employees.html',{'employees':employees})

@login_required
def employeedetail(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'shop/employeedetail.html',{'employee':employee})

@login_required
def employeeadd(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        form=EmployeeForm()
    return render(request,'shop/employeeadd.html',{'form':form})

@login_required
def employeeedit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'shop/employeeedit.html',{'employee':employee})

@login_required
def employeeupdate(request,id):
    if request.method=='POST':
        employee=Employee.objects.get(id=id)
        employee.name=request.POST['name']
        employee.contact=request.POST['contact']
        employee.address=request.POST['address']
        employee.gender=request.POST['gender']
        employee.desg=request.POST['desg']
        employee.qual=request.POST['qual']
        employee.experience=request.POST['experience']
        employee.save()
        return HttpResponseRedirect('/employees')

@login_required
def employeedelete(request,id):
    Employee.objects.get(id=id).delete()
    return HttpResponseRedirect('/employees')

@login_required
def search(request):
    if request.method=='POST':
        input=request.POST['search']
        query=(Q(orderid__icontains=input) | Q(name__icontains=input) | Q(contact__icontains=input) | Q(orderby__icontains=input) | Q(address__icontains=input) | Q(delivery_date__icontains=input) | Q(status__icontains=input) | Q(paymentmode__icontains=input))
        orders=Order.objects.filter(query)
        query=(Q(name__icontains=input) | Q(contact__icontains=input) | Q(address__icontains=input) | Q(gender__icontains=input) | Q(qual__icontains=input) | Q(desg__icontains=input) | Q(experience__icontains=input))
        employees=Employee.objects.filter(query)
        query=(Q(name__icontains=input) | Q(contact__icontains=input) | Q(address__icontains=input) | Q(website__icontains=input))
        dealers=Dealer.objects.filter(query)
        query=(Q(productid__icontains=input) | Q(name__icontains=input) | Q(description__icontains=input) | Q(price__icontains=input) | Q(stock__icontains=input))
        products=Product.objects.filter(query)
    return render(request,'shop/search.html',{'orders':orders,'employees':employees,'products':products,'dealers':dealers})

@login_required
def generatePDF(request,id):
        date=datetime.now()
        order=Order.objects.get(id=id)
        data={
            'order':order,
            'date':date,
        }
        pdf=render_to_pdf('shop/orderinvoice.html',data)
        if pdf:
            return HttpResponse(pdf,content_type="application/pdf")
            filename="Invoice_%s.pdf" %(filename)
            download=request.GET.get("download")
            if download:
                content="attachment;filename='%s'" %(filename)
            response['Content-Disposition'] =content
            return response
        return HttpResponse("Not found")