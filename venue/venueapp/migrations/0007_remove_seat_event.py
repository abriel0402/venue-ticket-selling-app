# Generated by Django 4.1 on 2023-01-14 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("venueapp", "0006_alter_seat_event"),
    ]

    operations = [
        migrations.RemoveField(model_name="seat", name="event",),
    ]