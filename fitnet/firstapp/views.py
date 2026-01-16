from django.shortcuts import render
def indexview(request):
    return render(request,'index.html')

def tAbout(request):
    return render(request,'tAbout.html')
# Create your views here.
