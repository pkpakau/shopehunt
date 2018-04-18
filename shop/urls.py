from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth

urlpatterns=[
    url(r'^dashboard',views.dashboard,name="dashboard"),
    url(r'^$',auth.login,{'template_name':'shop/login.html'},name="login"),
    url(r'^users/login',auth.login,{'template_name':'shop/login.html'},name="login"),
    url(r'^users/logout',auth.logout,{'next_page':'/'},name="logout"),
    url(r'^accounts/login',auth.login,{'template_name':'shop/login.html'},name="login"),

    url(r'^dealers/',views.dealers,name="dealers"),
    url(r'^dealer/products/(?P<id>\d+)/$',views.dealerproducts,name="dealerproducts"),

    url(r'^dealer/detail/(?P<id>\d+)/$',views.dealerdetail,name="dealerdetail"),
    url(r'^dealer/add',views.dealeradd,name='dealeradd'),
    url(r'^dealer/edit/(?P<id>\d+)/$',views.dealeredit,name="dealeredit"),
    url(r'^dealer/update/(?P<id>\d+)/$',views.dealerupdate,name='dealerupdate'),
    url(r'^dealer/delete/(?P<id>\d+)/$',views.dealerdelete,name="dealerdelete"),

    url(r'^products/',views.products,name="products"),
    url(r'^product/detail/(?P<id>\d+)/$',views.productdetail,name="productdetail"),
    url(r'^product/add',views.productadd,name="productadd"),
    url(r'^product/edit/(?P<id>\d+)/$',views.productedit,name="productedit"),
    url(r'^product/update/(?P<id>\d+)/$',views.productupdate,name="productupdate"),
    url(r'^product/delete/(?P<id>\d+)/$',views.productdelete,name="productdelete"),

    url(r'^orders',views.orders,name="orders"),
    url(r'^order/detail/(?P<id>\d+)/$',views.orderdetail,name="orderdetail"),
    url(r'^order/add',views.orderadd,name="orderadd"),
    url(r'^order/edit/(?P<id>\d+)/$',views.orderedit,name="orderedit"),
    url(r'^order/update/(?P<id>\d+)/$',views.orderupdate,name="orderupdate"),
    url(r'^order/delete/(?P<id>\d+)/$',views.orderdelete,name="orderdelete"),
    url(r'^invoice/(?P<id>\d+)/$',views.generatePDF,name="pdf"),

    url(r'^employees',views.employees,name="employees"),
    url(r'^employee/detail/(?P<id>\d+)/$',views.employeedetail,name="employeedetail"),
    url(r'^employee/add',views.employeeadd,name="employeeadd"),
    url(r'^employee/edit/(?P<id>\d+)/$',views.employeeedit,name="employeeedit"),
    url(r'^employee/update/(?P<id>\d+)/$',views.employeeupdate,name="employeeupdate"),
    url(r'^employee/delete/(?P<id>\d+)/$',views.employeedelete,name="employeedelete"),

    url(r'^search',views.search,name="search"),
]