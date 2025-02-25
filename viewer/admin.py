from django.contrib import admin

from viewer.models import Genre, Movie, Actor

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
# books
# author
admin.site.register(Actor)