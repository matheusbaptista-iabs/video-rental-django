# Generated by Django 4.1.3 on 2022-12-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_itemstate_available_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Laguage',
            new_name='Language',
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(),
        ),
    ]