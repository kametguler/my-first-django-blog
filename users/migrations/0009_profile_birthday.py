# Generated by Django 3.1.6 on 2021-02-14 20:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210214_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 14, 20, 32, 27, 892120, tzinfo=utc), verbose_name='Doğum Tarihi'),
        ),
    ]
