# Generated by Django 3.0.6 on 2020-06-17 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='gmail',
            new_name='email',
        ),
    ]
