# Generated by Django 4.1.5 on 2023-03-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_remove_booking_booking_id_remove_bus_bus_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='price',
            field=models.IntegerField(default=150),
        ),
    ]
