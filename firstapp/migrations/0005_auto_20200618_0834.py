# Generated by Django 3.0.6 on 2020-06-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_email_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
    ]