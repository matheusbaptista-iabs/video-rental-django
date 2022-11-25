from django.db import models
from datetime import datetime


# Create your models here.

class Director(models.Model):
    director_name = models.CharField(max_length=250)

class Actor(models.Model):
    actor_name = models.CharField(max_length=250)

class Laguage(models.Model):
    language = models.CharField(max_length=250)

class Genre(models.Model):
    genre = models.CharField(max_length=250)

class ItemState(models.Model):
    name = models.CharField(max_length=250)
    available = models.BooleanField(default=True)

class Studio(models.Model):
    name = models.CharField(max_length=250)

class MediaType(models.Model):
    name = models.CharField(max_length=250)
    rental_price = models.FloatField()


class Film(models.Model):

    def __str__(self):
        return self.original_title

    original_title = models.CharField(max_length=250)
    english_title = models.CharField(max_length=250)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=250)
    image = models.ImageField()
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    language = models.ManyToManyField(Laguage)
    genre = models.ManyToManyField(Genre)
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)


    def is_released(self):
        release_date = self.release_date
        today_date = datetime.today()
        is_released = True if (today_date - release_date).days <= 180 else False
        return is_released


class Item(models.Model):
    bar_code = models.IntegerField()
    acquisition_date = models.DateTimeField()
    item_state = models.ForeignKey(ItemState, on_delete=models.DO_NOTHING)
    media_type = models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)

    def calculate_rental_price(self):
        rental_price = self.media_type.rental_price

        if self.film.is_released():
            rental_price = rental_price * 1.5

        return rental_price 