from django.shortcuts import render
def index2(request):
    return render(request,'tempadmin/index2.html')
def Useradmin(request):
    return render(request,'tempadmin/Useradmin.html')
def Traineradmin(request):
    return render(request,'tempadmin/Traineradmin.html')
def loginadmin(request):
    return render(request,'tempadmin/loginadmin.html')

