# Generated by Django 5.0.2 on 2024-03-08 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('disc', models.CharField(blank=True, max_length=500)),
                ('content', models.CharField(blank=True, max_length=2000)),
                ('image', models.FileField(blank=True, default='', upload_to='media/uploads')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
    ]