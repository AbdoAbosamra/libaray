from django.contrib import admin

from .models import Book

# Register model to admin panel
admin.site.register(Book)