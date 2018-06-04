# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('add_id', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]
