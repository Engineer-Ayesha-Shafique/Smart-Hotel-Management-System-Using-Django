# Generated by Django 4.1.4 on 2022-12-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_savedcarts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]