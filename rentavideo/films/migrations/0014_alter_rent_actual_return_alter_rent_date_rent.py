# Generated by Django 4.1.5 on 2023-02-03 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0013_remove_rent_film_alter_rent_actual_return_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='actual_return',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 15, 20, 26, 988828)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='date_rent',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 15, 20, 26, 988803)),
        ),
    ]
