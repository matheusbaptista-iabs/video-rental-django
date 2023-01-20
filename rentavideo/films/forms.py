from django import forms
from .models import Film, Rent, Item, ItemState, User

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['original_title', 'english_title', 'release_date', 'description', 'director', 'actor', 'language', 'genre', 'studio', 'image']
        
class RentalFilmForm(forms.ModelForm):

  def __init__(self, *args, film=None, **kwargs):
    super(RentalFilmForm, self).__init__(*args, **kwargs)
    # Filter and display only the available films
    self.fields['item'].queryset = Item.objects.filter(item_state=ItemState.objects.get(name='Available'), film_id=film)

 
  class Meta:
    model = Rent
    fields = ['item', 'date_rent']
      
    
class RentalReturnFilmForm(forms.ModelForm):
  class Meta:
    model = Rent
    fields = ['item', 'actual_return']