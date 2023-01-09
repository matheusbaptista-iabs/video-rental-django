from django.shortcuts import render
from .models import Client, User
from .forms import ClientForm, ClientRegisterForm
from django.views.generic import FormView

# Create your views here.

class CreateClient(FormView):
    model = User
    form_class = ClientRegisterForm
    template_name = 'clients/register.html'
    success_url = 'films/details.html'
    
class DetailsClient(FormView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/details.html'
    success_url = 'films/index.html'

