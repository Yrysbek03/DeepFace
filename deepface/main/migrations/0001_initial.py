# Generated by Django 4.0.4 on 2022-05-07 00:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('age', models.CharField(max_length=150)),
                ('ethnicity', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=10)),
                ('pixels', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]