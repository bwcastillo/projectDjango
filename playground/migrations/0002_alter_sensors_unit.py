# Generated by Django 4.1.4 on 2022-12-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sensors",
            name="unit",
            field=models.CharField(max_length=10),
        ),
    ]
