# Generated by Django 5.0.1 on 2024-04-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbannerthree',
            name='ad_image',
            field=models.ImageField(upload_to='ads/banner/'),
        ),
    ]
