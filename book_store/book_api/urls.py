from django.urls import path

from .views import display_books

urlpatterns = [
    path('', display_books, name="home_page"),
]