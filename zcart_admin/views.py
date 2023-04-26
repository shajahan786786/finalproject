import random
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from common.models import Seller

# Create your views here.

def master (request):
    return render(request, 'zcart_admin_templates/admin_master.html')

def home (request):
    return render(request, 'zcart_admin_templates/admin_home.html')

def customer_list (request):
    return render(request, 'zcart_admin_templates/customer_list.html')

def seller_list (request):
    return render(request, 'zcart_admin_templates/seller_list.html')



def approve_seller (request):
    to_approve_seller = Seller.objects.filter(status='to approve')
    
    return render(request, 'zcart_admin_templates/approve_seller.html',{'to_approve_seller':to_approve_seller})

def do_approve (request,pid):
    seller_approve  = Seller.objects.get(id = pid)
    seller_user_name = seller_approve.seller_name+'_'+str(random.randint(1111,9999))
    
    seller_pwd = 'sel- '+str(random.randint(1111,9999))
    message='hi your user name is '+str(seller_user_name)+'and temporary password is'+seller_pwd
    seller_email=seller_approve.email
    
    seller_approve.user_name = seller_user_name
    seller_approve.password = seller_pwd
    seller_approve.status = 'approved'
    seller_approve.save()
    send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email],
            fail_silently=False

        )
    
    return redirect('zcart_admin:approve_seller')
    



 