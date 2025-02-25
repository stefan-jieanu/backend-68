from django.db.models import *

# Create your models here.
class Author(Model):
    name = CharField(max_length=128)
    date_of_birth = DateField()

    def __str__(self):
        return self.name

class Book(Model):
    title = CharField(max_length=128)
    description = TextField()
    author = ForeignKey(Author, on_delete=DO_NOTHING)
    isbn = CharField(max_length=13)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title