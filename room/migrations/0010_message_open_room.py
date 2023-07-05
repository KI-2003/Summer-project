# Generated by Django 3.2.18 on 2023-06-24 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_open_room_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='open_room',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='room.open_room'),
        ),
    ]