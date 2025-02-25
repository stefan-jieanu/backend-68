from django.db import models
from django.db.models import *


# Create your models here.
class Genre(Model):

    # Schimba numele cu care este afisat modelul in pagina de admin
    # nu necesita rularea makemigrations sau migrate
    class Meta:
        verbose_name_plural = 'Genuri de film'

    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Actor(Model):
    name = CharField(max_length=128)
    date_of_birth = DateField()
    description = TextField()

    def __str__(self):
        return self.name


class Movie(Model):
    # CharField este field pentru text cu lugime mai scurta
    title = CharField(max_length=128)

    # ForeignKey leaga modelul de un alt model
    # on_delete = ce se intampla cand se sterge un obiect asociat
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)

    # IntegerField este folosit pentru un field de tip integer
    rating = IntegerField()

    # DateField este un field pentru o data cu zi, luna, an
    released = DateField()

    # TextField este folosit pentru sectiuni de text mai lungi
    description = TextField()

    actors = ManyToManyField(Actor)

    # DateTimeField contine zi, luna, an, ora, secunda
    # auto_now_add specifica acestui field sa se completeze singur,
    # automat cu data si ora actuala
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} -- {self.genre.name}'