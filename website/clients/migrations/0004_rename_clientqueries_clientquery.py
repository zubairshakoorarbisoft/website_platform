# Generated by Django 4.2.9 on 2024-01-29 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clientqueries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientQueries',
            new_name='ClientQuery',
        ),
    ]