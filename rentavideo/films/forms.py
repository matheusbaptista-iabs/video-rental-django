from django import forms
from .models import Film, Rent

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['original_title', 'english_title', 'release_date', 'description', 'director', 'actor', 'language', 'genre', 'studio', 'image']
        
class RentalFilmForm(forms.ModelForm):
    class Meta:
      model = Rent
      fields = ['client', 'item', 'date_rent', 'rental_count']
      
class RentalReturnFilmForm(forms.ModelForm):
  class Meta:
    model = Rent
    fields = ['item', 'actual_return']