from django.db import models
class trainer_Registration(models.Model):
    name=models.CharField(max_length=50)
    emailaddress=models.EmailField(max_length=60)
    contactnumber=models.CharField(max_length=10)
    experience=models.CharField(max_length=25)
    achievements=models.CharField(max_length=100)
    specification=models.CharField(max_length=100,null=True,blank=True)
    dateofbirth = models.DateField(null=False, blank=False)
    profileimg=models.ImageField(upload_to='doc_profileimg',default=True)
    certificate=models.ImageField(upload_to='doc_certificate',default=True)
    password=models.CharField(max_length=10)
    Expected_income=models.CharField(max_length=10,null=True,blank=True)
    adminapprove=models.BooleanField(default=False)
    adminreject=models.BooleanField(default=False)


    def __str__(self):
        return self.name 

class Trainer_Add_Slot(models.Model):
    Trainer=models.ForeignKey(trainer_Registration,on_delete=models.CASCADE)
    Day=models.CharField(max_length=10)
    Start_time=models.TimeField()
    End_time=models.TimeField()
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Trainer.name} - {self.Day} {self.Start_time}-{self.End_time}"
    



# Create your models here.
