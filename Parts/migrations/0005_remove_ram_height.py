# Generated by Django 4.0.8 on 2023-10-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parts', '0004_alter_aircooler_amazon_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ram',
            name='height',
        ),
    ]