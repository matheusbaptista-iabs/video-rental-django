from django.shortcuts import render
from .models import User
from .forms import ClientRegisterForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class CreateClient(FormView):
    model = User
    form_class = ClientRegisterForm
    template_name = 'clients/register.html'
    
    def get_success_url(self):
        return reverse('clients:login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class LoginClient(LoginView):
    template_name = 'clients/login.html'
    success_url = 'films/index.html' 
    
    def get_success_url(self):
        return reverse('films:index')
    
class LogoutClient(LogoutView):
    template_name = 'clients/logout.html'
    success_url = 'clients/login.html' 
    
    
    
    
    
    
    
    
    
    
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