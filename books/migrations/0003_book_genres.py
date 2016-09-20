# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='books.Genre'),
        ),
    ]
