from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
