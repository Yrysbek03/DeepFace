# Generated by Django 4.0.4 on 2022-05-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
