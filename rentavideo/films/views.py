from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from datetime import datetime
from films.models import Film, Rent, Item, ItemState
from films.forms import FilmForm, RentalFilmForm, RentalReturnFilmForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView
from django.urls import reverse, reverse_lazy

from django_tables2 import SingleTableView
from .tables import RentTable


# Create your views here.

class IndexFilm(ListView):
    model = Film
    template_name = 'films/index.html'
    context_object_name = 'videos'


class DetailFilm(DetailView):
    model = Film
    template_name = 'films/detail.html'
    pk_url_kwarg = 'pk_film'


class CreateFilm(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


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


class RentFilm(PermissionRequiredMixin, CreateView):
    model = Rent
    form_class = RentalFilmForm
    template_name = 'films/rent.html'
    success_url = reverse_lazy('films:index')
    permission_required = 'films.add_rent'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(film=Film.objects.filter(id=self.kwargs.get('pk_film')).first())
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.film = self.object.item.film

        item_to_rent = Item.objects.get(id=self.object.item.id)
        item_to_rent.item_state = ItemState.objects.get(name='Rented')
        item_to_rent.save()

        self.object.save()

        return HttpResponseRedirect(self.success_url)


class RentedVideosByClientView(ListView):
    model = Rent
    template_name = 'films/rented_movies.html'

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user, actual_return=None)


class ReturnMovieView(UpdateView):
    model = Rent
    form_class = RentalReturnFilmForm
    template_name = 'films/return_movie.html'
    success_url = reverse_lazy('films:index')

    def form_valid(self, form):
        rental = form.save(commit=False)
        rental.actual_return = datetime.now()
        rental.save()

        self.object.item.item_state = ItemState.objects.get(name='Available')
        self.object.item.save()

        return HttpResponseRedirect(self.success_url)


""" Admin section """


class HomeAdminView(SingleTableView):
    table_class = RentTable
    queryset = Rent.objects.all()
    template_name = 'administrator/index.html'
    paginate_by = 7


class RentDetailView(DetailView):
    model = Rent
    template_name = 'administrator/rent_detail.html'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        self.object = Rent.objects.get(id=self.kwargs['pk'])
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rent = self.get_object()
        context['total_price'] = rent.calculate_rental_fee()
        import pdb;pdb.set_trace()

        # Get user's personal details
        user = rent.user
        context['user_name'] = user.get_full_name()
        context['user_email'] = user.email

        # Get user's rental history
        rental_history = Rent.objects.filter(user=user).values('item__film__original_title', 'date_rent',
                                                               'actual_return')
        context['rental_history'] = rental_history
        # rental_history = Rent.objects.filter(user=user)
        # context['rental_history'] = rental_history

        return context


class RentDeleteView(DeleteView):
    model = Rent
    success_url = reverse_lazy('films:home_admin')
    template_name = 'administrator/rent_delete.html'
