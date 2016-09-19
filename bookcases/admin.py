from django.contrib import admin

from .models import Bookcase

class BookcaseAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Bookcase, BookcaseAdmin)