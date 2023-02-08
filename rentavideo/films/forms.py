from django import forms
from .models import Film, Rent, Item, ItemState, User
import datetime

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['original_title', 'english_title', 'release_date', 'description', 'director', 'actor', 'language', 'genre', 'studio', 'image']
        
class RentalFilmForm(forms.ModelForm):

  def __init__(self, *args, film=None, **kwargs):
    super(RentalFilmForm, self).__init__(*args, **kwargs)
    # Filter and display only the available films
    self.fields['item'].queryset = Item.objects.filter(item_state=ItemState.objects.get(name='Available'), film=film)

 
  class Meta:
    model = Rent
    fields = ['item', 'date_rent']
    labels = {
      'date_rent': 'Date of Rental',
    }
      
    
class RentalReturnFilmForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super(RentalReturnFilmForm, self).__init__(*args, **kwargs)
    self.initial['actual_return'] = datetime.datetime.now()

  class Meta:
    model = Rent
    widgets = {
      'actual_return': forms.DateTimeInput(
        attrs={'class': 'form-control', 'readonly': True})
    }
    fields = ['actual_return']
    labels = {
      'actual_return': 'Return Date',
    }