# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-12 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0017_auto_20180610_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='ip',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
    ]
