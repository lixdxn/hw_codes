# Generated by Django 5.0.6 on 2024-05-10 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/')),
                ('draft', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('date', models.DateField()),
                ('car_color', models.CharField(choices=[('blue', 'Blue'), ('green', 'Green'), ('red', 'Red'), ('yellow', 'Yellow'), ('black', 'Black')], max_length=20)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.manufacture')),
            ],
        ),
    ]
