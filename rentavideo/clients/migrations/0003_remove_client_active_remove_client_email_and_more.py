# Generated by Django 4.1.5 on 2023-02-03 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_responsible_alter_client_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='active',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
    ]