from django.db import models
from newadmin.models import *
from trainer.models import *
from django.utils import timezone
# Create your models here.
class User_Registration(models.Model):
    fullname=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=60)
    phonenumber=models.CharField(max_length=10)
    dateofbirth =models.CharField(max_length=15)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=50)
    age=models.CharField(max_length=6,null=True)
    password=models.CharField(max_length=10)
    profileimage=models.ImageField(upload_to='userprofile/',null=True)
    height = models.IntegerField(null=True, blank=True)   # cm
    weight = models.IntegerField(null=True, blank=True)   # kg
    allergies = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.fullname

class trainer_booking(models.Model):
    Trainer=models.ForeignKey(trainer_Registration,on_delete=models.CASCADE)
    user=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    slot_id=models.ForeignKey(Trainer_Add_Slot,on_delete=models.CASCADE,null=True)
    slot=models.CharField(max_length=30,null=True)
    Expected_income=models.CharField(max_length=30,null=True)
    is_booked=models.BooleanField(default=False)
    paystatus=models.BooleanField(default=False)
    booked_date=models.DateTimeField(default=timezone.now)
    health_issues=models.CharField(max_length=200,null=True)
    notes=models.CharField(max_length=30,null=True)
    Goal=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.fullname

class product_booking(models.Model):
        product=models.ForeignKey(GymProduct,on_delete=models.CASCADE)
        user=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
        payment_status=models.BooleanField(default=False)
        booking_status=models.BooleanField(default=False)
        pname=models.CharField(max_length=30,null=True)
        price=models.CharField(max_length=20,null=True)
        des=models.CharField(max_length=100,null=True)
        booking_date=models.DateTimeField(default=timezone.now)
        nadmin=models.ForeignKey(newadmin,on_delete=models.CASCADE,null=True)
        def __str__(self):
            return self.user.fullname
         
    
# trainer (foreign key)
# user (foreign key)
# producct
# payment_status
# booking status
# date
# admin foreign key 



    # emailaddress=models.EmailField(max_length=60)
    # phonenumber=models.CharField(max_length=10)
    # date=models.CharField(max_length=15)
    # time=models.CharField(max_length=10)
    # address=models.CharField(max_length=50)

    # def __str__(self):
    #     return self.trainername     

    

