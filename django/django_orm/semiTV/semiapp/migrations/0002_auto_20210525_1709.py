# Generated by Django 2.2.4 on 2021-05-25 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tv',
            old_name='Realease_date',
            new_name='Release_date',
        ),
    ]
