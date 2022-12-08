from django.shortcuts import render
from films.models import Film, Rent
from films.forms import FilmForm, RentalFilmForm, RentalReturnFilmForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView

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
    
    
class RentFilm(FormView):
    model = Rent
    form_class = RentalFilmForm
    template_name = 'films/rent.html'
    success_url = 'films/index.html'
    
class ReturnFilm(FormView):
    model = Rent
    form_class = RentalReturnFilmForm
    template_name = 'films/return.html'
    success_url = 'films/index.html'