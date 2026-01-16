from django.urls import path,include 
from .import views
urlpatterns=[
    path('',views.indexview,name="indexview"),
    path('tAbout',views.tAbout,name='tAbout'),
   

]
