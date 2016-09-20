from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    wikipedia_url = models.URLField(blank=True)
    date_added = models.DateTimeField(default=timezone.now, null=True, blank=True)
    bookshelf = models.ForeignKey('bookcases.Bookshelf', null=True, blank=True)
    authors = models.ManyToManyField('Author')
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    FICTION = 'fiction'
    NON_FICTION = 'non-fiction'

    CATEGORY_CHOICES = (
        (FICTION, 'Fiction',),
        (NON_FICTION, 'Non-fiction'),
    )
    
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, 
        default=NON_FICTION, choices=CATEGORY_CHOICES)
