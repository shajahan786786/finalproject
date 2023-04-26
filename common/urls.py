from django.urls import path
from . import views
app_name='common'
urlpatterns = [
    
    path('',views.commonhome, name='commonhome'),
    path('customer_registration',views.customer_registration, name='customer_registration'),
    path('seller_registration',views.seller_registration, name='seller_registration'),
    path('customer_login',views.customer_login, name='customer_login'),
    path('seller_login',views.seller_login, name='seller_login'),
    path('c_forget_pwd',views.c_forget_pwd, name='c_forget_pwd'),
    path('s_forget_pwd',views.s_forget_pwd, name='s_forget_pwd'),
    path('mail_exist',views.mail_exist,name='mail_exist'),
    path('seller_mail_exist',views.seller_mail_exist,name='seller_mail_exist')
    
    
]