# Generated by Django 4.1.3 on 2023-01-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0018_alter_userorder_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userorder",
            name="order",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="userorder",
            name="username",
            field=models.CharField(max_length=200),
        ),
    ]
