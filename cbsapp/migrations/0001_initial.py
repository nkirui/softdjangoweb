# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', tinymce.models.HTMLField()),
                ('Email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=50)),
                ('Cell', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
