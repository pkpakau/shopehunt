from django.forms import ModelForm
from shop.models import Dealer,Product,Order,Employee

class DealerForm(ModelForm):
    class Meta:
        model=Dealer
        fields=('name','contact','address','website')
        

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=('dealer','productid','name','description','price','stock','image',)

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=('name','contact','address','gender','desg','qual','experience','image')

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=('orderid','name','contact','orderby','address','delivery_date','status','paymentmode','price')