from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='client_user')
    cep = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    cpf = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=100)
    birth = models.DateField()

    def __str__(self):
        return self.user.username


    

