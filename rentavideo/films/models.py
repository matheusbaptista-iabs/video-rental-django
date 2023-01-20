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
        return '%s - %s - %s' % (self.user, self.film.original_title, self.item.bar_code)
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='rented_item')
    date_rent = models.DateTimeField(default=datetime.now())
    actual_return = models.DateTimeField(default=datetime.now())

    
    def calculate_final_rental_price(self):
   
        rental_count = self.rental_count * 3
        predicted_return = self.date_rent + timedelta(rental_count)
        # valor de fato

        if (self.actual_date - self.date_rent).days <= self.rental_count:
            print(5 * self.rental_count * self.item.calculate_rental_price)
        else:     
            print(10 * self.rental_count * self.item.calculate_rental_price)
        
        return self.calculate_final_rental_price
        
        
        # if date_diff <= 0:
        #     return 10 * self.rental_count * self.item.calculate_rental_price
        
        # else:
            
        
        
        
        
        
        

        # if self.rental_count % 3 == 0:    
        #     return 10 * self.rental_count * self.item.calculate_rental_price
    
        # elif self.rental_count % 3 != 0 and self.rental_count > 3:
        #     return 15 * self.rental_count * self.item.calculate_rental_price
        
        # else:
        #     return 8 * self.rental_count * self.item.calculate_rental_price
            
        
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     rental_price = self.item.media_type.rental_price

    #     if self.item.calculate_rental_price():
    #         rental_price = rental_price * 1.5
            
    #         if (date_return - date_rent).days / 3:
    #             return rental_price * 10 * (date_return - date_rent).days / 3
            
    #         predicted_return_date = abs((date_return - date_rent).days)
    #         return_date = rental_price * new_rental_count
            
    #     else:
            
            

    #     return rental_price 
        
        
        
      
    
    # def is_delaied(...) #multa