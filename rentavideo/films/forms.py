from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['original_title', 'english_title', 'release_date', 'description', 'director', 'actor', 'language', 'genre', 'studio', 'image']
        
#class DetailFilmForm(forms.ModelForm):
  #  class Meta:
   