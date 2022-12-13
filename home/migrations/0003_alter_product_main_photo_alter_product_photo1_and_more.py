# Generated by Django 4.1.4 on 2022-12-13 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_photo',
            field=models.ImageField(upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 12, 50, 38, 303475)),
        ),
    ]