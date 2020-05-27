from django.contrib import admin
from .models import Book

class BookModel(admin.ModelAdmin):
	pass


admin.site.register(Book, BookModel)