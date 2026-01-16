from django.urls import path
from .import views
urlpatterns=[
     path('UserRegistration',views.UserRegistration,name="UserRegistration"),
     path('UserLogin',views.UserLogin,name="UserLogin"),
      path('Userhome',views.Userhome,name="Userhome"),
      path('Utrainer',views.Utrainer,name="Utrainer"),
      path('UTBook<int:cid>',views.UTBook,name="UTBook"),
      path('UDiet',views.UDiet,name="UDiet"),
      path('UProfile',views.UProfile,name="UProfile"),
      path('Utask',views.Utask,name="Utask"),
      path('Udetails<int:vid>',views.Udetails,name='Udetails'),
      path('Upayment_details',views.Upayment_details,name="Upayment_details"),
      path('bookingpay<int:id>',views.bookingpay,name="bookingpay"),
      # path('', views.Userhome, name='user_home'),
      path('product_details/<int:pid>/', views.product_details, name='product_details'),
      path('book-product/<int:pid>/', views.book_product, name='book_product'),
      path('Ucart', views.Ucart, name='Ucart'),
      path('Product_payment', views.Product_payment, name='Product_payment'),
      path('remove_cart<int:id>', views.remove_cart, name='remove_cart'),

      

 





]

