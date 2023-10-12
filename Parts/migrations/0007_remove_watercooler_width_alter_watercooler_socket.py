# Generated by Django 4.0.8 on 2023-10-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parts', '0006_remove_watercooler_size_alter_aircooler_socket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watercooler',
            name='width',
        ),
        migrations.AlterField(
            model_name='watercooler',
            name='socket',
            field=models.CharField(choices=[('AM5', 'AM5'), ('AM4', 'AM4'), ('LGA 1700', 'LGA 1700'), ('LGA 1200', 'LGA 1200'), ('LGA 1151', 'LGA 1151'), ('AMD and Intel', 'AMD and Intel')], max_length=20),
        ),
    ]
