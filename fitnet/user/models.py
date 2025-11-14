from django.db import models

# Create your models here.
class User_Registration(models.Model):
    fullname=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=60)
    phonenumber=models.CharField(max_length=10)
    dateofbirth =models.CharField(max_length=15)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=10)