from django.urls import path

from viewer.views import MoviesView, movie_detail_view, genres, MoviesByGenreView, MovieCreateView, MovieUpdateView, \
    MovieDeleteView, add_review_view, ReviewDeleteView, all_reviews

urlpatterns = [
    # Cand folosim CBV (Class Based Views) in path() trebuie sa adaugam
    # NumeleView.as_view()
    path('', MoviesView.as_view(), name='movies'),
    path('<pk>', movie_detail_view, name='movies_detail'),
    path('genres/', genres, name='genres'),
    path('genres/<genre_id>', MoviesByGenreView.as_view(), name='movies_by_genre'),
    path('create/', MovieCreateView.as_view(), name='movies_create'),
    path('update/<pk>', MovieUpdateView.as_view(), name='movies_update'),
    path('delete/<pk>', MovieDeleteView.as_view(), name='movies_delete'),
    path('review/create/<movie_id>', add_review_view, name='add_review'),
    path('review/delete/<pk>', ReviewDeleteView.as_view(), name='delete_review'),
    path('review/<movie_id>', all_reviews, name='reviews')
]