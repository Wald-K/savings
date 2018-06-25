# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('interest', models.DecimalField(decimal_places=2, max_digits=4)),
                ('start_date', models.DateField()),
                ('stop_date', models.DateField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Bank')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Client')),
            ],
        ),
    ]