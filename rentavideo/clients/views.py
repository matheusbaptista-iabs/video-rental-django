from django.shortcuts import render
from .models import Client, User
from .forms import ClientForm, ClientRegisterForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.

class CreateClient(FormView):
    model = User
    form_class = ClientRegisterForm
    template_name = 'clients/register.html'
    success_url = 'clients/details.html'
    
class DetailsClient(UpdateView):
    model = Client
    form_class = ClientForm
    pk_url_kwarg = 'pk' 
    template_name = 'clients/details.html'
    success_url = 'films/index.html'


class LoginClient(LoginView):
    template_name = 'clients/login.html'
    success_url = 'films/index.html' 
    
    
    
    
    
    
    
    
    
    
    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, context={'form':form})
    
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         user = authenticate(
    #             username=form.cleaned_data['username'],
    #             password=form.cleaned_data['password'],
    #         )
    #         if user is not None:
    #             login(request, user)
    #             return redirect('home')
    #     return render(request, self.template_name, context={'form':form})