from django.urls import path

from books.views import BooksView, BooksDetail, BooksCreate

urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('<pk>', BooksDetail.as_view(), name='book_detail'),
    path('create/', BooksCreate.as_view(), name='books_create')
]