# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('last_name', models.CharField(max_length=25)),
                ('birth_date', models.DateField()),
                ('city_of_birth', models.CharField(max_length=25)),
            ],
        ),
    ]
