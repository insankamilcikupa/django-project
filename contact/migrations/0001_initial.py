# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-10 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=50)),
                ('no_telp', models.CharField(blank=True, max_length=13)),
            ],
        ),
    ]
