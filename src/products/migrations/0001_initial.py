# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-09-18 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, default=30.99, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
