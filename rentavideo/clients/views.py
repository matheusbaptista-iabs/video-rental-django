from django.shortcuts import render
from clients.models import Client
from django.views.generic.edit import CreateView

# Create your views here.

class CreateClient(CreateView):
    model = Client;
    fields = ['username', 'first_name', 'last_name', 'email', 'cep', 'address', 'cpf', 'phone', 'birth']
    template_name: 'clients/client-form.html'
