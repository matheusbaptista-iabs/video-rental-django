from django.urls import path
from clients import views

app_name = "clients"

urlpatterns = [
    
    path('register', views.CreateClient.as_view(), name='register'),
    path('details/<username>/', views.DetailsClient.as_view(), name='details'),
    path('login', views.LoginClient.as_view(), name='login'),

    
   ]