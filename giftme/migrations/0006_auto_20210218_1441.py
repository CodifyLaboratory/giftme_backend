# Generated by Django 3.0.6 on 2021-02-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftme', '0005_auto_20210216_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='wish_pic/', verbose_name='Фото моего желания'),
        ),
    ]