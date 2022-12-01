from django.urls import path
from films import views

app_name = "films"

urlpatterns = [
    
    path('', views.IndexFilm.as_view(), name='index'),
    path('create', views.CreateFilm.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailFilm.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateFilm.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteFilm.as_view(), name='delete'),
    ]