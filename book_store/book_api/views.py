from django.shortcuts import render

from .models import Book

# Create your views here.
def display_books(request):
    books=Book.objects.all()
    print(type(books))
    print(books)
    return render(request, 'index.html', {'books':books})

