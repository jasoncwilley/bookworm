# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0003_auto_20160920_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('wikipedia_url', models.URLField(blank=True)),
                ('date_added', models.DateTimeField(blank=True, null=True, default=django.utils.timezone.now)),
                ('authors', models.ManyToManyField(to='books.Author')),
                ('bookshelf', models.ForeignKey(to='bookcases.Bookshelf', blank=True, null=True)),
            ],
        ),
    ]
