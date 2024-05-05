# Generated by Django 5.0.3 on 2024-03-28 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('synonyms', models.CharField(blank=True, max_length=100)),
                ('formula', models.CharField(blank=True, max_length=50)),
                ('CAS', models.CharField(max_length=15)),
                ('molecular_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=10)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('units', models.CharField(max_length=10)),
                ('reagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.reagent')),
            ],
        ),
    ]