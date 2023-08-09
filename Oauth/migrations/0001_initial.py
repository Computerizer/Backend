# Generated by Django 4.0.8 on 2023-08-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, default='Users/profile-pics/default-profile-pic.jpg', upload_to='Users/profile-pics')),
                ('sub_to_newsletter', models.BooleanField(default=True)),
                ('own_pc', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, null=True)),
                ('staff', models.BooleanField(default=False, null=True)),
                ('admin', models.BooleanField(default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
