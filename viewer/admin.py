from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Genre, Movie, Actor

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(Actor)

class MovieAdmin(ModelAdmin):

    @staticmethod
    # parametrul obj este un obiect de tip Movie
    # valoarea returnata de functie va fi pusa in tabel
    def released_year(obj):
        return obj.released.year

    @staticmethod
    # parametrul queryset contine toate filmele selectate din pagina
    def cleanup_description(modeladmin, request, queryset):
        # functia update() schimba un field cu valoarea specificata
        queryset.update(description='')

    actions = ['cleanup_description']

    # Ordinea in care apar obiectele in tabelul din admin
    # Ne putem folosi de orice proprietate din model
    ordering = ['title', 'released', 'rating']

    # Field-urile care vor aparea in tabelul din admin
    list_display = ['id', 'title', 'genre', 'released_year']

    # Field-urile care vor fi link-uri catre pagina cu detalii
    list_display_links = ['id', 'title']

    # Cate film vor aparea pe o pagina
    list_per_page = 10

    # Proprietati dupa care putem filtra filme
    list_filter = ['genre', 'actors', 'released']

    # Un camp de cautare
    search_fields = ['title']

    # Afecteaza doar pagina cu detalii
    # definim strucura paginii in felul urmator:
    # ('Nume sectiune', {'fields': ['nume field'], 'description': 'descriere sectiune'})
    fieldsets = [
        (
            'Essential information',
            {
                'fields': ['title', 'genre']
            }
        ),
        (
            'Extra info',
            {
                'fields': ['rating', 'released', 'description', 'actors', 'created'],
                'description': 'informatii extra despre film'
            }
        )
    ]

    readonly_fields = ['created']


admin.site.register(Movie, MovieAdmin)