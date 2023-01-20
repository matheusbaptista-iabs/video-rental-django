# Generated by Django 4.1.3 on 2023-01-19 13:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_alter_rent_actual_return_alter_rent_date_rent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='film_name', to='films.film'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rent',
            name='actual_return',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 13, 39, 27, 576523)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='date_rent',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 13, 39, 27, 576511)),
        ),
    ]
