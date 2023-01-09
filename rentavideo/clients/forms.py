from django import forms
from .models import Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClientRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'cep', 'address', 'cpf', 'phone', 'birth']