from django.contrib import admin
from booksmodel.models import Books
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'publisher','timestamp']

admin.site.register(Books,BooksAdmin)