from django.db import models
class trainer_Registration(models.Model):
    fullname=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=60)
    contactnumber=models.CharField(max_length=10)
    experience=models.CharField(max_length=25)
    dateofbirth =models.CharField(max_length=15)   
    profileimg=models.imagefield(upload_to='doc',default=True)
    certificate=models.imagefield(upload_to='doc',default=True)
    password=models.CharField(max_length=10)                                                                                                                                                                          

# Create your models here.
