from django.urls import path
from clients.views import *

app_name = "clients"

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('signup/', ClientSignUpView.as_view(), name='signup'),
    path('login/', ClientLoginView.as_view(), name='login'),
    
   ]