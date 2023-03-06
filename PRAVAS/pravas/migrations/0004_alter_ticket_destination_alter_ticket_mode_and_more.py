# Generated by Django 4.1.5 on 2023-02-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pravas', '0003_remove_ticket_travel_date_remove_tour_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='destination',
            field=models.CharField(choices=[('Morbi', 'Morbi'), ('Deesa', 'Deesa'), ('Vadodara', 'Vadodara'), ('Rajkot', 'Rajkot'), ('Anand', 'Anand'), ('Mahesana', 'Mahesana'), ('Nadiad', 'Nadiad'), ('Navsari', 'Navsari'), ('Jamnagar', 'Jamnagar'), ('Surat', 'Surat'), ('Ahmedabad', 'Ahmedabad')], default='Ahmedabad', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='mode',
            field=models.CharField(choices=[('Bus', 'Bus'), ('Plane', 'Plane'), ('Train', 'Train')], default='Bus', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='operators',
            field=models.CharField(choices=[('Kabra', 'Kabra'), ('Tulsi', 'Tulsi'), ('GSRTC', 'GSRTC'), ('Bharat', 'Bharat')], default='GSRTC', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='source',
            field=models.CharField(choices=[('Morbi', 'Morbi'), ('Deesa', 'Deesa'), ('Vadodara', 'Vadodara'), ('Rajkot', 'Rajkot'), ('Anand', 'Anand'), ('Mahesana', 'Mahesana'), ('Nadiad', 'Nadiad'), ('Navsari', 'Navsari'), ('Jamnagar', 'Jamnagar'), ('Surat', 'Surat'), ('Ahmedabad', 'Ahmedabad')], default='Ahmedabad', max_length=50),
        ),
    ]
