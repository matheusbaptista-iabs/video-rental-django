from datetime import datetime

from django import forms
from .models import Client
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClientSignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientSignUpForm, self).__init__(*args, **kwargs)
        try:
            usuario = kwargs.get('instance').user
            self.fields['username'].initial = usuario.username
            self.fields['first_name'].initial = usuario.first_name
            self.fields['last_name'].initial = usuario.last_name
            self.fields['email'].initial = usuario.email
        except:
            self.fields['username'].initial = None
            self.fields['first_name'].initial = None
            self.fields['last_name'].initial = None
            self.fields['email'].initial = None


    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="Your Username")

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Maria'}), label="First Name")

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Santos'}), label="Last Name")

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'maria-santos@gmail.com'}), label="Email")

    cep = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '70000'}), label="CEP (ZIP Code)")

    birth = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'max': datetime.now().date()}), label="Date of Birth")

    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rua Rio Vermelho, 500'}), label="Address")

    cpf = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="CPF (ID number)")

    phone = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="Phone")

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'The password must have at least 6 digits'}),
        label="Write your Password"
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Repeat the password above'}),
        label="Confirm your Password"
    )


    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Wrong Passwords')
        elif len(password1) and len(password2) < 6:
            raise ValidationError('Password is too short')
        else:
            return self.cleaned_data

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'cep', 'cpf', 'phone', 'birth', 'password1', 'password2']
