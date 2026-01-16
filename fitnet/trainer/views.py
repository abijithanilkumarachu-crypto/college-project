from django.shortcuts import render,redirect
from.models import *
from user.models import *
from django.contrib import messages

def TrainerRegistration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        emailaddress=request.POST.get('email')
        contactnumber=request.POST.get('contactnumber')
        experience=request.POST.get('experience')
        achievements=request.POST.get('Achievements')
        dateofbirth = request.POST.get('dateofbirth')
        profileimg=request.FILES.get('profileimg')
        certificate=request.FILES.get('certificate')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        Payment=request.POST.get('Payment')
        if password!=cpassword:
            messages.error(request,'Password does not match')
            return render(request,'trainer/TrainerRegistration.html')
        else:
            reg=trainer_Registration(name=name,emailaddress=emailaddress,contactnumber=contactnumber,achievements=achievements,
            dateofbirth=dateofbirth,experience=experience,profileimg=profileimg,certificate=certificate,password=password,Expected_income=Payment)
            reg.save()
            return redirect('TrainerLogin')
    else:
            messages.success(request,'Registration Successful')
            return render(request,'trainer/TrainerRegistration.html')
    
    return render(request,'trainer/TrainerRegistration.html')
def TrainerLogin(request):
    if request.method=="GET":
        return render(request,'trainer/TrainerLogin.html')
    else:
        try:
            emailaddress=request.POST.get('emailaddress')
            password=request.POST.get('password')
            error_message=NameError
            flag=0
            obj=trainer_Registration.objects.get(emailaddress=emailaddress)
            print(obj.emailaddress,obj.password)
            if obj and obj.adminapprove==1 :
                print("logged in")
                if(password==obj.password):
                    flag=1
                if flag==1:   
                    request.session['trainerid']=obj.id
                    request.session['trainername']=obj.name
                    return redirect('Trainerhome')
                else:
                        error_message='Email or Password Invalid !!!'
                        return render(request,'trainer/TrainerLogin.html',{'error':error_message})
            else:
                if obj.adminapprove==0:
                    error_message='Admin has not approved your registration yet'

        except trainer_Registration.DoesNotExist as e:
            error_message='Email or Password Invalid !!!'
            return render(request,'trainer/TrainerLogin.html',{'error':error_message})
    return render(request,'trainer/TrainerLogin.html',{'error':error_message})

    



def Trainerhome(request):
    return render(request,'trainer/Trainerhome.html')
def Add_Slot(request):
    trainer_id=request.session['trainerid']

    if request .method=='POST':
        trainer_id=request.session['trainerid']
        # trainer=trainer_Registration.objects.get(id=trainer_id)
        Day=request.POST.get('Day')
        start_time=request.POST.get('start_time')
        end_time=request.POST.get('end_time')
        sl=Trainer_Add_Slot(Trainer_id=request.session['trainerid'],Day=Day,Start_time=start_time,End_time=end_time)
        sl.save()
        messages.success(request,'Slot added successfully')
        return redirect('View_Slot')
    return render(request,'trainer/Add_Slot.html',{'m':trainer_id})

def View_Slot(request):
    data=Trainer_Add_Slot.objects.filter(Trainer_id=request.session['trainerid'])
    return render(request,'trainer/View_Slot.html',{'da':data})

def About(request):
    return render(request,'trainer/About.html')
def Task(request):
    return render(request,'trainer/Task.html')                             
def User_details(request):
    udet=trainer_booking.objects.filter(Trainer=request.session['trainerid'],is_booked=True)
    return render(request,'trainer/User_Details.html', {'udet': udet})
def Diet(request):
    return render(request,'trainer/Diet.html')
def User_Profile(request,uid):
    data=User_Registration.objects.get(id=uid)
    # userbookings=trainer_booking.objects.filter(user=uid,Trainer=request.session['trainerid'],is_booked=True)
    userbookings = trainer_booking.objects.filter(
    user=uid,
    Trainer=request.session['trainerid'],
    is_booked=True).first()

    return render(request,'trainer/User_Profile.html',{'user':data,'userbookings':userbookings})
def Tdelete(request,sid):
    data=Trainer_Add_Slot.objects.get(id=sid)
    data.delete()
    return redirect('View_Slot')