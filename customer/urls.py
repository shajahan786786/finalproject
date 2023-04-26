from django.urls import path
from . import views
app_name='customer'
urlpatterns = [
    
    path('',views.customerhome, name='customerhome'),
    path('products',views.products, name='products'),
    path('customer/product/<int:pid>/', views.product_details, name='product_details'),
    path('cart',views.cart, name='cart'),
    path('delete_item/<int:pid>', views.delete_item, name='delete_item'),
    # path('purchase', views.purchase, name='purchase'),
    path('change_pwd', views.change_pwd, name='change_pwd'),
    path('logout', views.logout_view, name='logout'),
    path('sale/', views.sale, name='sale'),
    
    
    
]