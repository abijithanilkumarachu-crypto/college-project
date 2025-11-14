from django.shortcuts import render,redirect
from.models import User_Registration
from django.contrib import messages   
def UserRegistration(request):
     if request.method == 'POST':

          fullname = request.POST.get('name')
          emailaddress = request.POST.get('email')
          phonenumber = request.POST.get('phone')
          dateofbirth = request.POST.get('dob') 
          gender = request.POST.get('gender') 
          address = request.POST.get('address') 
          password = request.POST.get('password') 
          confirmpassword = request.POST.get('confirm_password')
          if password==confirmpassword:
               if User_Registration.objects.filter(emailaddress=emailaddress).exists():
                    messages.info(request,'This email address is already in use')
               elif User_Registration.objects.filter(phonenumber=phonenumber).exists():
                 messages.info(request,'This phone number is already in use' )
               else:
                 userdata = User_Registration(fullname=fullname,emailaddress=emailaddress,phonenumber=phonenumber,
                                              dateofbirth=dateofbirth ,gender= gender,address=address,password=password)
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
     return render(request,'user/Userhome.html')
def Utrainer(request):
     return render(request,'user/Utrainer.html')
def UTDetails(request):
     return render(request,'user/UTDetails.html')
def UTBook(request):
     return render(request,'user/UTBook.html')
def UDiet(request):
     return render(request,'user/UDiet.html')
def UProfile(request):
     return render(request,'user/UProfile.html')
def Utask(request):
     return render(request,'user/Utask.html')



