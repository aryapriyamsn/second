# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-12 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mob_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]