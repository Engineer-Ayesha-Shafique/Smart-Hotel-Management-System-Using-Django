# Generated by Django 3.1.6 on 2021-02-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_zones', '0005_auto_20210211_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]
