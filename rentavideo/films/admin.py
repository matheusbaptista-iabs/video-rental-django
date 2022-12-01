from django.contrib import admin
from .models import Film, MediaType, Studio, ItemState, Director, Actor, Language, Genre, Item
# Register your models here.

admin.site.register(Film)
admin.site.register(MediaType)
admin.site.register(Studio)
admin.site.register(ItemState)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Item)
