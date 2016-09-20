from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    wikipedia_url = models.URLField(blank=True)
    date_added = models.DateTimeField(default=timezone.now, null=True, blank=True)
    bookshelf = models.ForeignKey('bookcases.Bookshelf', null=True, blank=True)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
