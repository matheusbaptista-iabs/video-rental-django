# Generated by Django 4.1.5 on 2023-02-07 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0016_alter_rent_actual_return_alter_rent_date_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='actual_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='date_rent',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 15, 13, 4, 876272)),
        ),
    ]
