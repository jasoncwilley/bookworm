from django.db import models

class Bookcase(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Bookshelf(models.Model):
    shelf_label = models.CharField(max_length=50)
    bookcase = models.ForeignKey('Bookcase')

    class Meta:
        ordering = ['shelf_label',]
        verbose_name_plural = 'bookshelves'

    def __str__(self):
        return "{} in {}".format(self.shelf_label, self.bookcase.name)