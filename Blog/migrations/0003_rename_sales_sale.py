# Generated by Django 4.0.4 on 2022-10-29 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_sales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]