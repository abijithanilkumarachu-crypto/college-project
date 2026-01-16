from django.urls import path
from .import views
urlpatterns=[
       path('index2',views.index2,name="index2"),
       path('Useradmin',views.Useradmin,name="Useradmin"),  
       path('Traineradmin',views.Traineradmin,name="Traineradmin"),
       path('loginadmin',views.loginadmin,name="loginadmin"),
       path('ProductDetails',views.ProductDetails,name="ProductDetails"),
       path('add_product',views.add_product,name='add_product'),
       path('Aupdate<int:sid>',views.Aupdate,name='Aupdate'),
       path('Adelete<int:sid>',views.Adelete,name='Adelete')
       


]