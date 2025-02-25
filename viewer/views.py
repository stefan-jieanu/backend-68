from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from viewer.forms import MovieForm
from viewer.models import Movie, Genre


def home(request):
    site_title = 'HollyMovies'
    animals = ['bear', 'lion', 'dog']

    return render(
        request,
        template_name='home.html',
        context={
            'title': site_title,
            'animals': animals
        }
    )


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_queryset(self):
        # Rulam functia de originala care returneaza toate filmele
        qs = super().get_queryset()

        return qs.order_by('released')


class MoviesDetailView(DetailView):
    template_name = 'movies_detail.html'
    model = Movie


def genres(request):
    g = Genre.objects.all()

    return render(
        request,
        template_name='genres.html',
        context={'genres': g}
    )


class MoviesByGenreView(ListView):
    template_name = 'movies_by_genre.html'
    model = Movie

    # Redefinim felul in care sunt luate filmele din baza de date
    def get_queryset(self):
        # Rulam functia de originala care returneaza toate filmele
        qs = super().get_queryset()

        # self.kwargs este un dictionar care contine parametrii din url
        g = Genre.objects.get(id=self.kwargs['genre_id'])
        return qs.filter(genre=g)


# FormView este o clasa pentru un formular generic
# class MovieCreateView(FormView):
#     template_name = 'movies_form.html'
#     form_class = MovieForm
#
#     # success_url este link-ul la care vom fi trimisi dupa completarea formularului
#     # functia reverse_lazy() ne va returna un path definit in urls.py dupa nume
#     success_url = reverse_lazy('movies') # /movies
#
#     # In functia de form_valid noi putem face orice cu datele primite
#     # ex: salvam un obiect in baza de date, trimitem un email cu ele, etc
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#
#         Movie.objects.create(
#             title = cleaned_data['title'],
#             genre = cleaned_data['genre'],
#             rating = cleaned_data['rating'],
#             released = cleaned_data['released'],
#             description = cleaned_data['description']
#         )
#
#         return result
#
#     # Functia se apeleaza automat atunci cand formularul nu este valid
#     def form_invalid(self, form):
#         print('Formularul nu este valid')
#         return super().form_invalid(form)

class MovieCreateView(CreateView):
    template_name = 'movies_form.html'
    form_class = MovieForm

    # success_url este link-ul la care vom fi trimisi dupa completarea formularului
    # functia reverse_lazy() ne va returna un path definit in urls.py dupa nume
    success_url = reverse_lazy('movies')
