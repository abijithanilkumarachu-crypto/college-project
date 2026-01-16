from turtle import up
from urllib import request
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages  
from trainer.models import * 
from django.shortcuts import render
from newadmin.models import GymProduct  
from django.shortcuts import render, get_object_or_404, redirect
from .models import GymProduct, product_booking, User_Registration

global amount

from fitnet.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
def UserRegistration(request):
     if request.method == 'POST':

          fullname = request.POST.get('name')
          emailaddress = request.POST.get('email')
          phonenumber = request.POST.get('phone')
          dateofbirth = request.POST.get('dob') 
          age= request.POST.get('age')
          profileimage= request.FILES.get('profileimage')
          gender = request.POST.get('gender') 
          address = request.POST.get('address') 
          # height = request.POST.get('height')
          # weight = request.POST.get('weight')
          # allergies = request.POST.get('allergies')
          password = request.POST.get('password') 
          confirmpassword = request.POST.get('confirm_password')
          if password==confirmpassword:
               if User_Registration.objects.filter(emailaddress=emailaddress).exists():
                    messages.info(request,'This email address is already in use')
               elif User_Registration.objects.filter(phonenumber=phonenumber).exists():
                 messages.info(request,'This phone number is already in use' )
               else:
                 userdata = User_Registration(fullname=fullname,emailaddress=emailaddress,phonenumber=phonenumber,
                                              dateofbirth=dateofbirth ,gender= gender,address=address,password=password,age=age,profileimage=profileimage)
                 userdata.save()
                 return redirect("UserLogin")                                                                                                                                                                                                                                                                                                                                                   
          else:
            messages.info(request,'password not matched')
     return render(request,'user/UserRegistration.html')         
def UserLogin(request):
     if request.method=="POST":
          try:
              emailaddress=request.POST.get('email')
              password=request.POST.get('password')
              user=User_Registration.objects.get(emailaddress=emailaddress,password=password)
              request.session['user_id']=user.id
              request.session['user_name']=user.fullname          
              return redirect('Userhome')
          except User_Registration.DoesNotExist:
               messages.info(request,'Invalid email or password')
     return render(request,'user/UserLogin.html')
def Userhome(request):
    products = GymProduct.objects.all()
    return render(request,'user/Userhome.html', {
        'da': products
         })
def Utrainer(request):
     data=trainer_Registration.objects.all()
     return render(request,'user/Utrainer.html', {'data': data})
def Udetails(request, vid):
     details=trainer_Registration.objects.get(id=vid)
     st=Trainer_Add_Slot.objects.filter(Trainer=vid)
     if request.method=="POST":
          trainer=request.POST.get('trainer_id')
          Expected_income=request.POST.get('Expected_income')
          health_issues=request.POST.get('health_issues')
          notes=request.POST.get('notes')
          user=request.session['user_id']
          Goal = request.POST.get("Goal")
          booking=trainer_booking(Trainer_id=trainer,user_id=user,Expected_income=Expected_income,health_issues=health_issues,notes=notes,Goal=Goal,is_booked=True)
          booking.save()
          messages.info(request,'Trainer booked successfully')
     return render(request,'user/UTDetails.html', {'details': details, 'st': st})
def UTBook(request, cid):
     da=Trainer_Add_Slot.objects.filter(Trainer=cid)
     t=trainer_Registration.objects.get(id=cid)

     return render(request,'user/UTBook.html', {'da': da})
def UDiet(request):
     return render(request,'user/UDiet.html')
def UProfile(request):
     up=User_Registration.objects.get(id=request.session['user_id'])
     if request.method == "POST":
        if request.FILES.get("profileimage"):
            up.profileimage = request.FILES["profileimage"]

        up.fullname = request.POST.get("fullname")
        up.phonenumber = request.POST.get("phonenumber")
        up.address = request.POST.get("address")
        up.height = request.POST.get("height")
        up.weight = request.POST.get("weight")
        up.allergies = request.POST.get("allergies")
        up.weight = request.POST.get("weight")

        up.save()

        return redirect("UProfile")
     return render(request,'user/UProfile.html', {'up': up})          
def Utask(request):
     return render(request,'user/Utask.html')     
def Upayment_details(request):
     ud=request.session['user_id']
     pb=trainer_booking.objects.filter(user=ud,is_booked=True)
     return render(request,'user/Upayment_details.html', {'pb': pb})


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def bookingpay(request, id):
    global amount
    
    pa=trainer_booking.objects.get(id=id)
    amount=pa.Expected_income
    api_key=RAZORPAY_API_KEY
#     amt=int(amount)*100
    amt=int(amount)*100
    currency = "INR"
  
    payment_order = client.order.create(dict(amount=amt, currency="INR", payment_capture=1))
    payment_order_id = payment_order['id']
    trainer_booking.objects.filter(user=request.session['user_id']).update(paystatus=True)
    return render(request, 'user/bookingpay.html', {'a': amount, 'api_key': api_key, 'order_id': payment_order_id})

def product_details(request, pid):
    
    product = get_object_or_404(GymProduct, id=pid)
    if request.method == "POST":
        pt=GymProduct.objects.get(id=pid)
        product = get_object_or_404(GymProduct, id=pid)
        user = User_Registration.objects.get(id=request.session['user_id'])
        pname=request.POST.get('product_name')
        price=request.POST.get('price')
        des=request.POST.get('description')
        product_booking.objects.create(
            product=pt,
            user=user,
               pname=pname,
               price=price,
               des=des,
            booking_status=False
        )
        messages.success(request, "Product added to cart successfully")
    return render(request, 'user/product_details.html', {
        'product': product
    })
def book_product(request, pid):
    if request.method == "POST":
        pt=GymProduct.objects.get(id=pid)
        product = get_object_or_404(GymProduct, id=pid)
        user = User_Registration.objects.get(id=request.session['user_id'])
        pname=request.POST.get('product_name')
        price=request.POST.get('price')
        des=request.POST.get('description')
        product_booking.objects.create(
            product=pid,
            user=user,
               pname=pname,
               price=price,
               des=des,
            booking_status=False
        )
        messages.success(request, "Product added to cart successfully")

        return redirect('product_details')

# def Ucart(request):
#      ad=product_booking.objects.filter(user=request.session['user_id'])
#      sum=0       
#      for i in ad:
#             sum += int(i.price)
#             global amount
#             amount=sum
#      return render(request,'user/Ucart.html', {'ad': ad,'sum':sum})
def Ucart(request):
    ad = product_booking.objects.filter(user=request.session['user_id'])
    global amount

    amount = sum(int(i.price.replace('₹','')) for i in ad)
    return render(request,'user/Ucart.html', {'ad': ad, 'sum': amount})



client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def Product_payment(request):
    global amount
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    currency = "INR"
    payment_order = client.order.create(dict(amount=amt, currency="INR", payment_capture=1))
    payment_order_id = payment_order['id']
    product_booking.objects.filter(user=request.session['user_id']).update(checkout_status=True)
    return render(request, 'user/Product_payment.html', {'a': amount, 'api_key': api_key, 'order_id': payment_order_id})

def remove_cart(request, id):
    item = product_booking.objects.get(id=id)
    item.delete()
    return redirect('Ucart')




    