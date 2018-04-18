from django.contrib import admin
from shop.models import Dealer,Product,Order,Employee
# Register your models here.
admin.site.register(Dealer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Employee)