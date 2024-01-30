# Generated by Django 4.2.9 on 2024-01-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_title', models.CharField(max_length=100)),
                ('no_of_positions', models.IntegerField()),
                ('is_remote', models.BooleanField()),
                ('is_on_site', models.BooleanField()),
                ('job_description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('last_date_to_apply', models.DateField()),
                ('domain', models.CharField(max_length=200)),
            ],
        ),
    ]
