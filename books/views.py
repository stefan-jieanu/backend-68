from django.shortcuts import render

from books.models import Book


# Create your views here.
def books(request):
    books = Book.objects.all()

    return render(
        request,
        'books.html',
        context={
            'books': books
        }
    )

def book_detail(request, id):
    book = Book.objects.get(id=id)

    return render(
        request,
        'books_detail.html',
        context={
            'book': book
        }
    )