# Generated by Django 5.0.2 on 2024-03-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_subservices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_1_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_2_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_3_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='benefit_4_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='h1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='h2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='section2_content',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='section_2_h2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='section_3_h2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_1_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='service_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_2_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='service_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_3_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='service_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_4_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='service_5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_5_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='service_6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='service_6_disc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.SlugField(max_length=200),
        ),
        migrations.DeleteModel(
            name='SubServices',
        ),
    ]