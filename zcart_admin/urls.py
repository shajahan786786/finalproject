from django.urls import path
from . import views
app_name='zcart_admin'
urlpatterns = [
    
    path('master',views.master, name='master'),
    path('home',views.home, name='home'),
    path('approve_seller',views.approve_seller, name='approve_seller'),
    path('do_approve/<int:pid>',views.do_approve, name='do_approve'),
    path('customer_list',views.customer_list, name='customer_list'),
    path('seller_list',views.seller_list, name='seller_list'),
    
    
    
]