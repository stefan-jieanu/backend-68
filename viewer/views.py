from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from viewer.forms import MovieForm
from viewer.mixins import StaffRequiredMixin
from viewer.models import Movie, Genre

# @login_required
def home(request):
    # site_title = 'HollyMovies'
    # animals = ['bear', 'lion', 'dog']
    #
    # return render(
    #     request,
    #     template_name='home.html',
    #     context={
    #         'title': site_title,
    #         'animals': animals
    #     }
    # )

    # Functia redirect va trimite inapoi la browser un Response de Redirect
    # Asta insemna ca vom fi trimisi la pagina mentionata
    # return redirect('https://google.com')
    return redirect('movies')


class MoviesView(PermissionRequiredMixin, ListView):
    template_name = 'movies.html'
    model = Movie

    # Structura permisiuni in interiorul unui cu PermissionRequiredMixin
    # permission_required = numeaplicatie.numeactiune_numemodel
    # Unde numeactiunie poate fi: view, add, change, delete
    permission_required = 'viewer.view_movie'

    def get_queryset(self):
        # Rulam functia de originala care returneaza toate filmele
        qs = super().get_queryset()

        return qs.order_by('released')


class MoviesDetailView(StaffRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'movies_detail.html'
    model = Movie
    permission_required = 'viewer.view_movie'


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


# 5 HTTP Request methods:
# GET - used for getting data
# POST - used for sending data
# DELETE - used for deleting data
# PUT - used for updating entire objects, if it doesn't exist create a new one
# PATCH - used for partially updating data


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'movies_form.html'
    form_class = MovieForm
    permission_required = 'viewer.add_movie'

    # success_url este link-ul la care vom fi trimisi dupa completarea formularului
    # functia reverse_lazy() ne va returna un path definit in urls.py dupa nume
    success_url = reverse_lazy('movies')


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'movies_form.html'
    form_class = MovieForm
    model = Movie
    permission_required = 'viewer.change_movie'

    success_url = reverse_lazy('movies')


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    permission_required = 'viewer.delete_movie'
    success_url = reverse_lazy('movies')
