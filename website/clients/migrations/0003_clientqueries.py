# Generated by Django 4.2.9 on 2024-01-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_testimonial_company_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientQueries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('company_name', models.FileField(upload_to='')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('requirements', models.CharField(max_length=10000, null=True)),
            ],
        ),
    ]
