from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from films.models import Film, Rent, Item, ItemState
from films.forms import FilmForm, RentalFilmForm, RentalReturnFilmForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView
from django.urls import reverse

# Create your views here.

class IndexFilm(ListView):
    model = Film
    template_name = 'films/index.html'
    context_object_name = 'videos'



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
        kwargs.update(film=Film.objects.filter(id=self.kwargs.get('pk_film')).first())
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

class RentedVideosByClientView(ListView):
    model = Rent
    template_name = 'films/rented_movies.html'
    #context_object_name = 'videos'


    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user, actual_return=None)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.user
    #     return context


def calculate_rental_fee(rental):
    rental_period = timezone.now() - rental.date_rent
    base_fee = 10
    extra_fee = 2 * (rental_period.days - 3)
    if extra_fee < 0:
        extra_fee = 0
    rental_fee = base_fee + extra_fee
    return rental_fee


class ReturnMovieView(UpdateView):
    model = Rent
    form_class = RentalReturnFilmForm
    template_name = 'films/return_movie.html'

    # def get_object(self, queryset=None):
    #     rental = get_object_or_404(Rent, id=self.kwargs['rent_id'])
    #     return rental

    def form_valid(self, form):
        rental = form.save(commit=False)
        rental.actual_return = timezone.now()
        rental.save()

        item_to_return = Item.objects.get(id=self.object.item.id)
        item_to_return.item_state = ItemState.objects.get(name='Available')
        item_to_return.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        return dict(
            super().get_context_data(**kwargs),
            rental_price=calculate_rental_fee(self.object))

    def get_success_url(self):
        return reverse('films:index')
        
    

    




    
# class ReturnFilm(FormView):
#     model = Rent
#     form_class = RentalReturnFilmForm
#     template_name = 'films/return_movie.html'
#     success_url = 'films/index.html'