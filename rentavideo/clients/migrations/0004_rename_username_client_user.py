# Generated by Django 4.1.5 on 2023-02-03 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_remove_client_active_remove_client_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='username',
            new_name='user',
        ),
    ]
