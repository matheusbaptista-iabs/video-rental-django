import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from .forms import ClientSignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from clients.models import Client
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.

class ClientSignUpView(CreateView):
    model = Client
    form_class = ClientSignUpForm
    template_name = 'clients/signup.html'
    success_url = reverse_lazy('clients:login')
    
    def form_valid(self, form):

        client = form.save(commit=False)
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            is_active=True,
            date_joined=datetime.datetime.now(),
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        user.groups.add(Group.objects.filter(name='RENT_FILM').first())
        client.user = user
        client.save()
        return HttpResponseRedirect(self.success_url)
    
    
class ClientLoginView(LoginView):
    template_name = 'clients/login.html'
    success_url = reverse_lazy('films:index')

    # def get_success_url(self):

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        return self.form_invalid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientSignUpForm
    template_name = 'clients/update.html'
    success_url = reverse_lazy('clients:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user.username = form.cleaned_data['username']
        self.object.user.first_name = form.cleaned_data['first_name']
        self.object.user.last_name = form.cleaned_data['last_name']
        self.object.user.email = form.cleaned_data['email']
        self.object.user.set_password(form.cleaned_data['password1'])
        self.object.save()
        self.object.user.save()
        return HttpResponseRedirect(self.success_url)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/detail.html'
    context_object_name = 'client'

class ClientListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    
