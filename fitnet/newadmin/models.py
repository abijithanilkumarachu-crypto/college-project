from django.db import models

# Create your models here.
class newadmin(models.Model):
   name=models.CharField(max_length=30)
   email=models.EmailField(max_length=60)
   password=models.CharField(max_length=30)


   def __str__(self):
        return self.name


# models.py
class GymProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    stock = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    def __str__(self):
        return self.name
