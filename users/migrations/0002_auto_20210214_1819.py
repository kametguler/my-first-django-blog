# Generated by Django 3.1.6 on 2021-02-14 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='p_photo',
            new_name='profile_image',
        ),
    ]
