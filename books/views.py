from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Book


# This is generic module to take all models object and listed as a template page
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'