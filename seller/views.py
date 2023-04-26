from django.http import HttpResponse
from django.shortcuts import redirect, render

from seller.models import Product
from customer.models import Cart

# Create your views here.

def seller_home (request):
    return render(request, 'seller_templates/home.html')

def add_products (request):
    msg =''
    if request.method == 'POST':
        product_name = request.POST['prd_name']
        product_desc = request.POST['prd_des'] 
        product_stock = request.POST['prd_stock']
        product_price = request.POST['prd_price']
        product_image = request.FILES['prd_image']

        new_product = Product(
            prod_name = product_name,
            prod_des = product_desc,
            prod_stock = product_stock,
            prod_price = product_price,
            prod_image = product_image,
            seller_id = request.session['seller']

        )
        new_product.save()
        msg = 'Product added'
    return render(request, 'seller_templates/add_products.html',{'msg':msg})

def products (request):
    products = Product.objects.filter(seller=request.session['seller'])
   
    return render(request, 'seller_templates/products.html',{'products':products})


def logout_view(request):
    if 'seller' in request.session:
        del request.session['seller']
        request.session.flush()
        return redirect('common:seller_login')
    else:
        return HttpResponse("You are not logged in.")
