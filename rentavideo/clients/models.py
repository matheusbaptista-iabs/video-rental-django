from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# # Create your models here.

class Client(models.Model):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    cep = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    cpf = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=100)
    birth = models.DateField()
    active = models.BooleanField(default=True)
    responsible = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    
    
  
# class Rent(models.Model):
#     def __str__(self):
#         return self.id
#   #  def has_delay(self):
        
        
# class Reservation(models.Model):
#     def __str__(self):
#         return self.id
    
#     reservation_date = models.DateField(default=datetime.today())
#     notification_date = models.DateField(default=datetime.today())
    

    