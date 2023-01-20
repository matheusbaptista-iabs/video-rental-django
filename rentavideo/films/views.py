from django.http import HttpResponseRedirect
from django.shortcuts import render
from films.models import Film, Rent, Item, ItemState
from films.forms import FilmForm, RentalFilmForm, RentalReturnFilmForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView
from django.urls import reverse

# Create your views here.

class IndexFilm(ListView):
    model = Film
    template_name = 'films/index.html'



class DetailFilm(DetailView):
    model = Film
    template_name = 'films/detail.html'


class CreateFilm(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                "No URL to redirect to.  Either provide a url or define"
                " a get_absolute_url method on the Model."
                )
        return url

    
    


class UpdateFilm(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/update.html'
    success_url = 'films/create.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class DeleteFilm(DeleteView):
    model = Film
    form_class = FilmForm
    template_name = 'films/delete.html'
    success_url = 'films/index.html'
    
    
class RentFilm(CreateView):
    model = Rent
    form_class = RentalFilmForm
    template_name = 'films/rent.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(film=self.kwargs.get("pk"))
        return kwargs

    def get_success_url(self):
        return reverse('films:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.film = self.object.item.film

        item_to_rent = Item.objects.get(id=self.object.item.id)
        item_to_rent.item_state = ItemState.objects.get(name='Rented')
        item_to_rent.save()

        #self.object.item.item_state.id = ItemState.objects.get(name='Rented').id
        #self.object.save()
        # self.object.item.item_state.save()
        # a = Item.objects.get(id=self.object.item.id)
        # a.item_state = ItemState.objects.get(name='Rented')
        #a.save()
        return super().form_valid(form) #HttpResponseRedirect(self.success_url)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[]
   
        
    

    




    
class ReturnFilm(FormView):
    model = Rent
    form_class = RentalReturnFilmForm
    template_name = 'films/return.html'
    success_url = 'films/index.html'