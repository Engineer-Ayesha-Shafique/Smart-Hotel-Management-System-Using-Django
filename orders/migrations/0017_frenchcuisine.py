# Generated by Django 4.1.3 on 2023-01-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0016_rename_pakistancuisine_pakistanicuisine"),
    ]

    operations = [
        migrations.CreateModel(
            name="FrenchCuisine",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dish_name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]