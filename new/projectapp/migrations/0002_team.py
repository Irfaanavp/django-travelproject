# Generated by Django 4.2.5 on 2023-09-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='', verbose_name='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
