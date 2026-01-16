from django.shortcuts import render,redirect
from.models import *
from user.models import User_Registration
from trainer.models import trainer_Registration
import os 
def index2(request):
    
    return render(request,'tempadmin/index2.html')
def Useradmin(request):
    data=User_Registration.objects.all()
    return render(request,'tempadmin/Useradmin.html',{'da':data})
def Traineradmin(request):
    data=trainer_Registration.objects.all()
    return render(request,'tempadmin/Traineradmin.html',{'da':data})
def loginadmin(request):
     if request.method=="POST":
          try:
              email=request.POST.get('email')
              password=request.POST.get('password')
              admin=newadmin.objects.get(email=email,password=password)
              request.session['admin_id']=admin.id
              request.session['admin_name']=admin.name          
              return redirect('index2')
          except newadmin.DoesNotExist:
               messages.info(request,'Invalid email or password')
     return render(request,'tempadmin/loginadmin.html')

def ProductDetails(request):
    data=GymProduct.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        description=request.POST.get('description')
        image=request.FILES['image']
        GymProduct.objects.create(name=name,price=price,stock=stock,description=description,image=image)
        return redirect('ProductDetails')
    return render(request,'tempadmin/ProductDetails.html',{'da':data})

def add_product(request):
    data = GymProduct.objects.all()
    return render(request, 'tempadmin/add_product.html', {'da': data})

def Aupdate(request, sid):
    data = GymProduct.objects.get(id=sid)
    if request.method == "POST":
        if 'image' in request.FILES:
            if data.image and os.path.isfile(data.image.path):
                os.remove(data.image.path)
            data.image = request.FILES['image']
        data.name = request.POST.get('name')
        data.price = request.POST.get('price')
        data.stock = request.POST.get('stock')
        data.description = request.POST.get('description')
        data.save()
        return redirect('ProductDetails')
    return render(request, 'tempadmin/Aupdate.html', {'da': data})
def Adelete(request, sid):
    data = GymProduct.objects.get(id=sid)
    data.delete()
    return redirect('ProductDetails')



