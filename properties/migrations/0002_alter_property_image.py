# Generated by Django 4.2.5 on 2023-09-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, upload_to='properties/images', verbose_name='image'),
        ),
    ]
