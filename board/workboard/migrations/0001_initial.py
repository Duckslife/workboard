# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('mail', models.CharField(blank=True, max_length=50)),
                ('memo', models.CharField(blank=True, max_length=200)),
                ('hit', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
