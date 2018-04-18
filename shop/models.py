from django.db import models

# Create your models here.
class Dealer(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.CharField(max_length=1000)
    website=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.name+"-"+str(self.contact)


class Product(models.Model):
    productid=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    image=models.FileField(upload_to='products')
    dealer=models.ForeignKey(Dealer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name+"-"+str(self.productid)+"-"+self.dealer

class Employee(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.CharField(max_length=1000)
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    gender=models.CharField(choices=GENDER,default="----",max_length=50)
    DESIGNATION=(
        ('Worker',"Worker"),
        ('Manager','Manager'),
        ('Board','Board')
    )
    desg=models.CharField(choices=DESIGNATION,default='Worker',max_length=50)
    qual=models.CharField(max_length=1000)
    experience=models.DecimalField(decimal_places=2,max_digits=10)
    image=models.FileField(upload_to='employees')
    def __str__(self):
        return self.name+"-"+self.desg

class Order(models.Model):
    orderid=models.CharField(max_length=10)
    name=models.CharField(max_length=200)
    contact=models.IntegerField()
    orderby=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    delivery_date=models.CharField(max_length=15)
    STATUS=(
        ('Received','Received'),
        ('Processing','Processing'),
        ('Completed','Completed'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered')
    )
    status=models.CharField(choices=STATUS,default='Received',max_length=50)
    MODE=(
        ('PostPay','PostPay'),
        ('HalfPay','HalfPay'),
        ('PostPay','PostPay'),
    )
    paymentmode=models.CharField(choices=MODE,default='PostPay',max_length=10)
    price=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.orderid+'-'+self.name