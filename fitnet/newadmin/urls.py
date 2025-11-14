from django.urls import path
from .import views
urlpatterns=[
      path('index2',views.index2,name="index2"),
       path('Useradmin',views.Useradmin,name="Useradmin"),  
       path('Traineradmin',views.Traineradmin,name="Traineradmin"),
       path('loginadmin',views.loginadmin,name="loginadmin")
]