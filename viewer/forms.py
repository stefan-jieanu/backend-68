import re
from datetime import date

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


# Validation/Cleaning in forms
# Partea de Validation ne va spune daca un field este Ok sau Nu Ok
# Daca nu este OK, vom returna o eroare cu un mesaj
# Partea de Cleaning implica schimbarea datelor din formular inainte de a le salva.

# 3 metode:
# A) declaram separat o functie validator in exterirul clasei pe care o putem refolosi in orice parte din formular
# B) creeam o noua clasa pornind de la o clasa de Field, si suprascriem metodele validate(), clean()
# C) declaram in interiorul clasei formular functii pentru fiecare field, sau pentru tot formularul:
# clean_numefield() care se aplica doar unui field
# clean() care se aplica tot formularului

# Metoda A
def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Title must be capitalized!')


# Metoda B
class PastMonthField(DateField):
    # Daca data introdusa este in viitor vom afisa utilizatorului o eroare
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past date allowed!')

    # Modificam data introdusa de utilizator in mod automat
    # Astfel incat sa fie mereu prima zi a lunii selectate de el/ea
    # Valoare returnata de functie va fi valoarea salavata in baza de date
    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):
    # Specificam detalii pentru formular
    class Meta:
        # Indicam modelul folosit
        model = Movie

        # Indicam fieldurile din model folsite in acest formular
        fields = '__all__'

        # Daca nu vrem sa includem toate fieldurile, le putem speifica
        # fields = ['title', 'genre', ]

    # Suprascriem functia __init__() pentru a modifica field-urile
    # atunci cand se genereaza formularul
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # visible_fields() va returna field-urile din formular
        # visile.field este obiectul din Python pentru acel field
        # visible.field.widget este HTML-ul generat pentru el
        # visible.field.attrs sunt atributele de HTML din acel field (ex: id, type, name, class, ...)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField(widget=DateInput)


    # Pentru fiecare field din formular exista o functie numita
    # clean_numefield
    # Valoare returnata de functie va fi valoarea salavata in baza de date
    def clean_description(self):
        # Capitalizam prima litera din fiecare propozitie
        # Initial text
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)


    # Un loc bun pentru a genera erori care apar din mai multe field-uri
    def clean(self):
        # variabila result este un dictionar cu toate field-urile din formular
        result = super().clean()
        if result['genre'].name == 'Comedy' and result['rating'] > 5:
            # Mesaj de eroare individual pentru un field
            self.add_error('genre', 'Comedy rating too high')
            self.add_error('rating', 'Comedy rating too high')

            # Mesaj de eroare generala pentru formular
            raise ValidationError('Comedies aren\'t good')

        return result
