# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-11 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0006_subscribepaper_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribepaper',
            name='skip',
            field=models.IntegerField(default=0),
        ),
    ]