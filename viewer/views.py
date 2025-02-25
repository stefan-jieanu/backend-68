from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from viewer.models import Movie, Genre


# Create your views here.
# def hello(request):
#     return HttpResponse('<h1>Hello World!</h1>')
#
# def new_page(request):
#     return HttpResponse('Pagina noua...')
#
# # Exemplu de view cu parametru tip regular exp
# def show_title(request, title):
#     return HttpResponse(f'Titlul este {title}')
#
# # Exemplu de view cu parametrii url encoded
# def show_params(request):
#     # Exemplu de link
#     # http://127.0.0.1:8000/show-params?nume=Mircea&varsta=20
#     # variabilele nume, varsta pot fi extrase din link cu functia
#     # request.GET.get('nume', '')
#     # Al doilea parametru al functiei get este returnat daca nu gaseste
#     # numele variabilei din link
#
#     name = request.GET.get('nume', '')
#     age = request.GET.get('varsta', '')
#     return HttpResponse(f'Numele meu este {name} si am {age} ani')

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

# View definit ca si functie
# def movies(request):
#     # Get all movies from database
#     # m = Movie.objects.all()
#
#     # Filter movies by genre
#     # genre = Genre.objects.get(name='Comedy')
#     # m = Movie.objects.filter(genre=genre)
#     # sau
#     # m = Movie.objects.filter(genre__name='Comedy')
#
#     # Filter by rating, exact
#     # m = Movie.objects.filter(rating=8)
#
#     # Filter by rating
#     # gt - greater than
#     # gte - greater than or equal
#     # lt - less than
#     # lte - less than or equal
#     # m = Movie.objects.filter(rating__gte=8)
#
#     # Filter by multiple criteria
#     # m = Movie.objects.filter(rating__lte=8).filter(genre__name='SciFi')
#
#     m = Movie.objects.all()
#
#     # Order movies alphabetically
#     # m = m.order_by('-title')
#
#     # Order movies by released date
#     m = m.order_by('-released')
#
#     # Return HTML template
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': m}
#     )
# *******************************************************
# SAU folosind Class Based Views
# *******************************************************
# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request,
#             template_name='movies.html',
#             context={
#                 'movies': Movie.objects.all()
#             }
#         )
# SAU folosind TemplateView
# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {
#         'movies': Movie.objects.all()
#     }
# SAU folosind ListView
class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_queryset(self):
        # Rulam functia de originala care returneaza toate filmele
        qs = super().get_queryset()

        return qs.order_by('released')

# def movies_detail(request, id):
#     m = Movie.objects.get(id=id)
#
#     return render(
#         request,
#         template_name='movies_detail.html',
#         context={'movie': m}
#     )
# SAU
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

# def movies_by_genre(request, genre_id):
#     g = Genre.objects.get(id=genre_id)
#     m = Movie.objects.filter(genre=g)
#
#     return render(
#         request,
#         template_name='movies_by_genre.html',
#         context={'movies': m, 'genre': g}
#     )
# SAU folosind ListView
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
