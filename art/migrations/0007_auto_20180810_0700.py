# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 07:00
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_categories_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='profilepicture',
            field=tinymce.models.HTMLField(),
        ),
    ]
