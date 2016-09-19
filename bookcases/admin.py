from django.contrib import admin

from .models import Bookcase, Bookshelf

class BookcaseAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('shelf_label', 'bookcase', )
    search_fields = ('shelf_label', 'bookcase__name', )
    list_filter = ('bookcase', )

admin.site.register(Bookcase, BookcaseAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)