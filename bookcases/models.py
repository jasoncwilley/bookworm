from django.db import models

class Bookcase(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name