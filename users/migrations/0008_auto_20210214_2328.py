# Generated by Django 3.1.6 on 2021-02-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210214_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Biyografi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, verbose_name='Telefon Numarası'),
        ),
    ]
