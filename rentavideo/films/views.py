from django.shortcuts import render
from films.models import Film
from films.forms import FilmForm
from django.views import CreateView, UpdateView

# Create your views here.

class CreateFilm(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/index.html'

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
    template_name = 'films/index.html'