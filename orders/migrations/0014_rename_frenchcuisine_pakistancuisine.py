# Generated by Django 4.1.3 on 2023-01-02 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0013_mexicancuisine_pakistanicuisine_turkishcuisine_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FrenchCuisine",
            new_name="PakistanCuisine",
        ),
    ]