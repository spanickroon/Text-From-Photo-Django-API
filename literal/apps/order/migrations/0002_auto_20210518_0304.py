# Generated by Django 3.2.2 on 2021-05-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="extension",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="language",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
