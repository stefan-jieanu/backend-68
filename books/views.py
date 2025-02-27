from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from books.forms import BookForm
from books.models import Book

class BooksView(ListView):
    template_name = 'books.html'
    model = Book


class BooksDetail(DetailView):
    template_name = 'books_detail.html'
    model = Book


class BooksCreate(CreateView):
    template_name = 'books_form.html'
    form_class = BookForm
    success_url = reverse_lazy('books')