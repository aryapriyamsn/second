# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-10 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0004_auto_20180410_1815'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='SubscribePaper',
        ),
    ]
