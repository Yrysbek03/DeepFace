# Generated by Django 4.0.4 on 2022-05-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_time_document_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='client_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='coffee_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
