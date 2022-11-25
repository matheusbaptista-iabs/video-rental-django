# Generated by Django 4.1.3 on 2022-11-23 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_title', models.CharField(max_length=250)),
                ('english_title', models.CharField(max_length=250)),
                ('release_date', models.DateTimeField()),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('actor', models.ManyToManyField(to='films.actor')),
                ('director', models.ManyToManyField(to='films.director')),
                ('genre', models.ManyToManyField(to='films.genre')),
                ('language', models.ManyToManyField(to='films.laguage')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.studio')),
            ],
        ),
        migrations.AddField(
            model_name='itemstate',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_code', models.IntegerField()),
                ('acquisition_date', models.DateTimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.film')),
                ('item_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.itemstate')),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.mediatype')),
            ],
        ),
    ]
