from django.db import models

# # Create your models here.

# class Client(models.Model):
#     def __str__(self):
#         return self.username

#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     cep = models.IntegerField()
#     address = models.CharField(max_length=150)
#     cpf = models.IntegerField(unique=True)
#     phone = models.IntegerField()
#     birth = models.DateField()