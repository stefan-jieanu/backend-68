from django.forms import *

from viewer.models import Genre, Movie


# Clasa create de noi pentru a afisa in formular un widget
# cu HTML-necesar pentru un calendar
class DateInput(DateInput):
    input_type = 'date'


# Form este o clasa pentru un formular generic
# class MovieForm(Form):
#     title = CharField(max_length=128)
#
#     # ModelChoiceField va genera un camp cu optiuni de selectat
#     # Unde optiunile vin din parametrul queryset
#     # Daca vrem ca optiunile sa fie dintr-un alt tabel, folosim:
#     # exemplu: NumeModel.objects
#     genre = ModelChoiceField(queryset=Genre.objects)
#
#     rating = IntegerField(min_value=1, max_value=10)
#     released = DateField(widget=DateInput)
#     description = CharField(widget=Textarea)

class MovieForm(ModelForm):
    # Specificam detalii pentru formular
    class Meta:
        # Indicam modelul folosit
        model = Movie

        # Indicam fieldurile din model folsite in acest formular
        fields = '__all__'

        # Daca nu vrem sa includem toate fieldurile, le putem speifica
        # fields = ['title', 'genre', ]

    rating = IntegerField(min_value=1, max_value=10)
    released = DateField(widget=DateInput)
