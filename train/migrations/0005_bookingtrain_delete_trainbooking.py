# Generated by Django 4.1.5 on 2023-04-03 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('train', '0004_remove_coachallocation_seat_seatallocation_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateField()),
                ('seat_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.seatallocation')),
                ('train_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='TrainBooking',
        ),
    ]
