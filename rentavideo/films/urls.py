from django.urls import path
from films import views

app_name = "films"

urlpatterns = [
    
    path('', views.IndexFilm.as_view(), name='index'),
    path('create', views.CreateFilm.as_view(), name='create'),
    path('detail/<int:pk_film>/', views.DetailFilm.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateFilm.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteFilm.as_view(), name='delete'),
    path('rent/add/item/<int:pk_film>/', views.RentFilm.as_view(), name='rent'),
    path('rentals/', views.RentedVideosByClientView.as_view(), name='rentals_by_client'),
    path('rentals/<int:pk>/return/', views.ReturnMovieView.as_view(), name='return_movie'),

    path('home/admin/', views.HomeAdminView.as_view(), name='home_admin'),
    path('home/admin/rent/<int:pk>/detail/', views.RentDetailView.as_view(), name='rent_detail'),
    path('home/admin/rent/<int:pk>/delete/', views.RentDeleteView.as_view(), name='rent_delete'),

]