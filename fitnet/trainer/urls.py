from django.urls import path
from .import views
urlpatterns=[
    path('TrainerRegistration',views.TrainerRegistration,name="TrainerRegistraion"),
    path('TrainerLogin',views.TrainerLogin,name='TrainerLogin'),
    path('Trainerhome',views.Trainerhome,name='Trainerhome'),
   path('Add_Slot',views.Add_Slot,name='Add_Slot'),
    path('View_Slot',views.View_Slot,name='View_Slot'),
     path('About',views.About,name='About'),
     path('Task',views.Task,name='Task'),
     path('User_details',views.User_details,name='User_details'),
     path('Diet',views.Diet,name='Diet'),
     path('User_Profile',views.User_Profile,name='User_Profile')

   
]
