# Generated by Django 3.1.1 on 2020-09-19 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_badges'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Badges',
            new_name='Badge',
        ),
    ]
