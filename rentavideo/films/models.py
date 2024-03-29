from django.utils import timezone

from django.db import models
from datetime import datetime, timedelta
from clients.models import User
import pdb


# Create your models here.

class Director(models.Model):
    director_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.director_name

class Actor(models.Model):    
    actor_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.actor_name

class Language(models.Model):
    language = models.CharField(max_length=250)
    
    def __str__(self):
        return self.language

class Genre(models.Model):
    genre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.genre

class ItemState(models.Model):
    name = models.CharField(max_length=250)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class MediaType(models.Model):
    name = models.CharField(max_length=250)
    rental_price = models.FloatField()
    
    def __str__(self):
        return self.name


class Film(models.Model):

    def __str__(self):
        return self.original_title

    original_title = models.CharField(max_length=250)
    english_title = models.CharField(max_length=250)
    release_date = models.DateField()
    description = models.CharField(max_length=250)
    image = models.ImageField()
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    language = models.ManyToManyField(Language) # write language
    genre = models.ManyToManyField(Genre)
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)


    def is_released(self):
        release_date = self.release_date
        today_date = datetime.today()
        is_released = True if (today_date - release_date).days <= 180 else False
        return is_released
    
    def verify_stock(self):  
        return Item.objects.filter(film_id=self.id).count()
    
    def is_item_available(self):
        return Item.objects.filter(film_id=self.id, item_state__available=True).count()


class Item(models.Model):
    bar_code = models.IntegerField()
    acquisition_date = models.DateTimeField()
    item_state = models.ForeignKey(ItemState, on_delete=models.DO_NOTHING)
    media_type = models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.film.original_title, self.bar_code)
    
    def is_available(self):
        if self.rented_item.exists():
            is_available = False
            if self.rented_item.last().actual_return:
                is_available = True
            else:
                is_available = False
        else:
            is_available = True if self.item_state.name == 'Available' else False
        return is_available
    
    def calculate_rental_price(self):
        rental_price = self.media_type.rental_price

        if self.film.is_released():
            rental_price = rental_price * 1.5            

        return rental_price 
    
    
class Rent(models.Model):
    
    def __str__(self):
        return '%s - %s - %s' % (self.user, self.item.film.original_title, self.item.bar_code)
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='rented_item')
    date_rent = models.DateTimeField(default=datetime.now())
    actual_return = models.DateTimeField(null=True, blank=True)

    def calculate_rental_fee(self):
        if self.actual_return:
            return 10

        rental_period = timezone.now() - self.date_rent
        base_fee = 10
        extra_fee = 2 * (rental_period.days - 3)
        if extra_fee < 0:
            extra_fee = 0
        rental_fee = base_fee + extra_fee
        return rental_fee

    def is_overdue(self):
        if self.actual_return is None and timezone.now() > (self.date_rent + timedelta(days=3)):
            return True
        else:
            return False

    def get_return_status(self):
        if self.actual_return:
            return 'Returned on ' + self.actual_return.strftime('%m/%d/%Y')
        elif self.is_overdue():
            return 'Overdue'
        else:
            return 'Not returned yet'

