# Generated by Django 3.2.18 on 2023-06-24 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_message_open_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='open_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='room.open_room'),
        ),
    ]
