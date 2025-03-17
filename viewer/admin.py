from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Genre, Movie, Actor

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(Actor)

class MovieAdmin(ModelAdmin):
    # Ordinea in care apar obiectele in tabelul din admin
    # Ne putem folosi de orice proprietate din model
    ordering = ['title', 'released', 'rating']

    # Field-urile care vor aparea in tabelul din admin
    list_display = ['id', 'title', 'genre']

    # Field-urile care vor fi link-uri catre pagina cu detalii
    list_display_links = ['id', 'title']

    # Cate film vor aparea pe o pagina
    list_per_page = 10

    # Proprietati dupa care putem filtra filme
    list_filter = ['genre', 'actors', 'released']

    # Un camp de cautare
    search_fields = ['title']


admin.site.register(Movie, MovieAdmin)