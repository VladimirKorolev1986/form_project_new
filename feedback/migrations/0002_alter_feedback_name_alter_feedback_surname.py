# Generated by Django 4.1.7 on 2023-05-09 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(max_length=60),
        ),
    ]