from django.urls import path
from .import views
urlpatterns=[
     path('UserRegistration',views.UserRegistration,name="UserRegistration"),
     path('UserLogin',views.UserLogin,name="UserLogin"),
      path('Userhome',views.Userhome,name="Userhome"),
      path('Utrainer',views.Utrainer,name="Utrainer"),
      path('UTDetails',views.UTDetails,name="UTDetails"),
      path('UTBook',views.UTBook,name="UTBook"),
      path('UDiet',views.UDiet,name="UDiet"),
      path('UProfile',views.UProfile,name="UProfile"),
      path('Utask',views.Utask,name="Utask")

]

