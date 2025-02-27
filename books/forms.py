from django.forms import *
from books.models import Book, Author
import re

class DateInput(DateInput):
    input_type = 'date'

# class BookForm(Form):
#     title = CharField(max_length=128)
#     author = ModelChoiceField(queryset=Author.objects)
#     created = DateField(widget=DateInput)
#     description = CharField(widget=Textarea)
#     isbn = CharField(max_length=13)

def title_validator(value):
    if re.search(r'[@#$%]', value):
        raise ValidationError("Titlul nu poate conține caracterele: @ # $ %")

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    title = CharField(max_length=128, validators=[title_validator])
    # author = ModelChoiceField(queryset=Author.objects)
    # created = DateField(widget=DateInput)
    description = CharField(widget=Textarea)
    isbn = CharField(max_length=13)

    def clean(self):
        result = super().clean()
        if result.get('title') == result.get('author').name:
            self.add_error('title', 'Titlul cartii nu poate fi acelasi cu numele autorului')
            self.add_error('author', 'Titlul cartii nu poate fi acelasi cu numele autorului')
        return result

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not re.fullmatch(r'\d{13}', isbn):
            raise ValidationError("ISBN-ul trebuie să aibă exact 13 caractere și să conțină doar cifre.")
        return isbn

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if re.search(r'[@#$%]', title):
    #         raise ValidationError("Titlul nu poate conține caracterele: @ # $ %")
    #     return title