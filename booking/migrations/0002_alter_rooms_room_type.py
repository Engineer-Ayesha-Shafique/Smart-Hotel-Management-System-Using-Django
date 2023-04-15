# Generated by Django 4.1.3 on 2023-01-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rooms",
            name="room_type",
            field=models.CharField(
                choices=[
                    ("1", "premium sweet"),
                    ("2", "deluxe sweet"),
                    ("3", "presidential sweet"),
                ],
                max_length=50,
            ),
        ),
    ]