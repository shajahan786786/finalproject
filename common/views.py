import random
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from common.models import Customer, Seller

# Create your views here.
def commonhome (request):
    return render(request, 'common_templates/home.html')

def customer_registration (request):
    msg=''
    if request.method == 'POST':
        customer_name = request.POST['c_name']
        customer_adress = request.POST['c_adress'] 
        customer_email = request.POST['c_email']
        customer_mobile = request.POST['c_mobile']
        customer_password = request.POST['c_pwd']
        

        new_customer = Customer(
            customer_name = customer_name,
            ph_number = customer_mobile,
            email = customer_email,
            adress = customer_adress,
            password = customer_password,
            

        )
        msg='Succesfully Registered  '
        new_customer.save()
    return render(request, 'common_templates/customer_registration.html',{'msg':msg})

def seller_registration (request):
    msg =''
    if request.method == 'POST':
        
        seller_name = request.POST['seller_name']
        seller_adress = request.POST['seller_adress'] 
        seller_email = request.POST['seller_email']
        seller_mobile = request.POST['seller_mobile']
        seller_company_name = request.POST['seller_company_name']
        seller_image = request.FILES['seller_image']
        seller_ifsc = request.POST['seller_ifsc']
        seller_branch = request.POST['seller_branch']
        seller_account = request.POST['seller_account']  
        seller_account_holder = request.POST['seller_account_holder']
        
        

        new_seller = Seller(
            seller_name = seller_name,
            address = seller_adress,
            email = seller_email,
            ph_num = seller_mobile,
            company_name = seller_company_name,
            image = seller_image,
            ifsc = seller_ifsc,
            branch_name = seller_branch,
            acc_no = seller_account,
            acc_holder_name = seller_account_holder,
            

        )
        msg='Registration is succesfull stay with us will update you soon '
        new_seller.save()
    return render(request, 'common_templates/seller_registraion.html',{'msg':msg})


def customer_login(request):
    
    msg=''
    if request.method == 'POST':
        
        customer_email = request.POST['c_email']
        customer_password = request.POST['c_pwd']
        try:
            customer= Customer.objects.get(email = customer_email,password = customer_password)
            request.session['customer'] = customer.id
            return redirect('customer:customerhome')
            # return redirect('customer:customer_home')
            
        except:
            msg = 'Invalid Userid or Password'

    return render(request, 'common_templates/customer_login.html',{'msg':msg})

def seller_login(request):
    
    msg=''
    if request.method == 'POST':
        
        seller_email = request.POST['s_email']
        seller_password = request.POST['s_pwd']
        
        try:
            seller= Seller.objects.get(email = seller_email,password = seller_password)
        
            request.session['seller'] = seller.id
            return redirect('seller:seller_home')
            
        except:
            msg = 'Invalid Userid or Password'

    return render(request, 'common_templates/seller_login.html',{'msg':msg})
def c_forget_pwd(request):
    
    msg =''
    if request.method=='POST':
        entered_email = request.POST['forget_mail']

        try:
            check=Customer.objects.get(email = entered_email)
            password=check.password
            send_mail(
                'your password is',
                password,
                settings.EMAIL_HOST_USER,
                [entered_email],
                fail_silently = False
            )
            msg='your password is send to your mail check it now'

        except:
            msg = 'enter registered email'

    return render(request, 'common_templates/customer_forget_pwd.html',{'msg':msg})

def s_forget_pwd(request):
    
    msg =''
    if request.method=='POST':
        entered_email = request.POST['forget_mail']

        try:
            check=Seller.objects.get(email = entered_email)
            password=check.password
            send_mail(
                'your password is',
                password,
                settings.EMAIL_HOST_USER,
                [entered_email],
                fail_silently = False
            )
            msg='your password is send to your mail check it now'

        except:
            msg = 'enter registered email'

    return render(request, 'common_templates/seller_forget_pwd.html',{'msg':msg})

def mail_exist(request):
    
    mail = request.POST['email']
   
    status = Customer.objects.filter(email= mail).exists()
    return JsonResponse({'status':status})

def seller_mail_exist(request):
    
    mail = request.POST['email']
   
    status = Seller.objects.filter(email= mail).exists()
    return JsonResponse({'status':status})