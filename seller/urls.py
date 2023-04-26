from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    
    path('',views.seller_home, name='seller_home'),
    path('add_products',views.add_products, name='add_products'),
    path('products',views.products, name='products'),
    path('logout',views.logout_view, name='logout')
    
    
    
]