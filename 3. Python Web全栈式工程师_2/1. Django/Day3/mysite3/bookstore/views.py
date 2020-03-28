from django.shortcuts import render

from .models import Book


# Create your views here.
def book(request):
    books = Book.objects.all()
    dict1 = {
        "books": books
    }
    return render(request, 'bookstore/book.html', dict1)
