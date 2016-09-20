from django.contrib import admin

from .models import Book, Author, Genre


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'authors__name']
    list_display = ['title', 'author_names']

    def author_names(self, obj):
        names = [author.name for author in obj.authors.all()]
        return ", ".join(names)

    author_names.short_description = 'Authors'

class BookInline(admin.StackedInline):
    model = Book.authors.through
    extra = 0

class BookGenreInline(admin.StackedInline):
    model = Book.genres.through
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline, ]
    search_fields = ['name', 'book__title', ]

class GenreAdmin(admin.ModelAdmin):
    inlines = [BookGenreInline, ]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)