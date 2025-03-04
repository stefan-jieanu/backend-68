from django.urls import path

from viewer.views import MoviesView, MoviesDetailView, genres, MoviesByGenreView, MovieCreateView, MovieUpdateView, \
    MovieDeleteView

urlpatterns = [
    # Cand folosim CBV (Class Based Views) in path() trebuie sa adaugam
    # NumeleView.as_view()
    path('', MoviesView.as_view(), name='movies'),
    path('<pk>', MoviesDetailView.as_view(), name='movies_detail'),
    path('genres/', genres, name='genres'),
    path('genres/<genre_id>', MoviesByGenreView.as_view(), name='movies_by_genre'),
    path('create/', MovieCreateView.as_view(), name='movies_create'),
    path('update/<pk>', MovieUpdateView.as_view(), name='movies_update'),
    path('delete/<pk>', MovieDeleteView.as_view(), name='movies_delete')
]