
import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import F
from common.models import Customer
from seller.models import Product
from zcart_erp.settings import BASE_DIR
from .models import Cart
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator


# Create your views here.


def customerhome (request):
    return render(request, 'customer_templates/customer_home.html')

def products (request):
    media_url = settings.MEDIA_URL 
    # productss = Product.objects.all()
    productss = Product.objects.all().values('id', 'prod_name', 'prod_des', 'prod_stock', 'prod_price', 'prod_image')
    paginator = Paginator(productss, 3) # 2 items per page
    page = request.GET.get('page')
    products = paginator.get_page(page) 
    
    return render(request, 'customer_templates/products.html',{'products':products,'MEDIA_URL':media_url})

def product_details(request,pid):
    msg = ''
    product  = Product.objects.get(id = pid)
    if request.method == 'POST':
        quantity = request.POST['qty']
        cart_exist = Cart.objects.filter(product_id = pid, customer_id = request.session['customer'] ).exists()
        if not cart_exist:  
            cart = Cart(customer_id = request.session['customer'], product_id = pid,quantity = quantity )
            cart.save()
            
            return redirect('customer:cart') 
        else:
            msg = 'Item already in cart'
    return render(request, 'customer_templates/product_details.html',{'product':product,'msg':msg})

def cart(request):
    cart_data = Cart.objects.filter(customer_id = request.session['customer']).annotate(total = F('product__prod_price')*F('quantity'))
    
    grand_total = 0    

    for products in cart_data:
        grand_total = products.total + grand_total
    request.session['grand_total'] = grand_total

    context = {
        'cart_data' : cart_data,
        'grand_total' : grand_total
    }    
    return render(request, 'customer_templates/cart.html',context)

def delete_item(request,pid):
    cart_item = Cart.objects.get(product=pid,customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')

# def purchase(request):
#     if request.method == 'POST':
#         for i, item in enumerate(cart_data):
#             quantity = request.POST.get(f'quantity{i+1}')
            
#     return redirect('customer:cart')
        
    
def change_pwd(request):
    msg = ''
    if request.method == 'POST':
        old_pwd = request.POST['old_pwd']
        new_pwd = request.POST['new_pwd']
        confirm_pwd = request.POST['confirm_pwd']
        
        customer = Customer.objects.get(id = request.session['customer'])
        if customer.password == old_pwd:
           
            if new_pwd == confirm_pwd:
                
                customer.password = new_pwd
                customer.save()
                msg = 'Password changed Succesfully'
            else:
                msg = 'Password does not match'

        else:
            
            msg = 'Incorrect Password'
    return render(request, 'customer_templates/pwd_change.html',{'msg':msg})

def sale(request):
    cart_data = Cart.objects.filter(customer_id=request.session['customer'])
    cart_total = sum([item.quantity * item.product.prod_price for item in cart_data])
    
    
    for item in cart_data:
        product = item.product
        product.prod_stock -= item.quantity
        product.save()
    cart_data_copy = list(cart_data)


    context = {
        'cart_data': cart_data_copy,
        'cart_total': cart_total,
    }
    
    # clear the cart after the sale
    cart_data.delete()
    request.session['grand_total'] = 0

    
    return render(request, 'customer_templates/sale.html', context)

def logout_view(request):
    
    
    if 'customer' in request.session:
        Cart.objects.filter(customer_id=request.session['customer']).delete() # This will delete all items from the user's cart
        del request.session['customer']
        request.session.flush()
        return redirect('common:customer_login')
    else:
        return HttpResponse("You are not logged in.")