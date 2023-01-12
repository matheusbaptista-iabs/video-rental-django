from django.urls import path
from clients import views

app_name = "clients"

urlpatterns = [
    
    path('register', views.CreateClient.as_view(), name='register'),
    path('login', views.LoginClient.as_view(), name='login'),
    path('logout', views.LogoutClient.as_view(), name='logout'),
    
   ]