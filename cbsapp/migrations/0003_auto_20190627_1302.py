# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-27 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbsapp', '0002_auto_20190627_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Company',
            new_name='user',
        ),
    ]
