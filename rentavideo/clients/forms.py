from django import forms
from .models import Client
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClientSignUpForm(forms.ModelForm):

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'User'}),)

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}),)

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}),)

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Write your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Confirm your password'}),
        strip=False,
    )

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Wrong Passwords')
        else:
            return self.cleaned_data


    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'cep', 'birth', 'address', 'cpf', 'phone', 'password1', 'password2']
        
