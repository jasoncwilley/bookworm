from django.contrib import admin

from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'authors__name']

class BookInline(admin.StackedInline):
    model = Book.authors.through
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline, ]
    search_fields = ['name', 'book__title', ]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)