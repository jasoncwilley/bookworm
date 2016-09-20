# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0002_bookshelf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookshelf',
            options={'ordering': ['shelf_label'], 'verbose_name_plural': 'bookshelves'},
        ),
    ]
