# Generated by Django 5.1.1 on 2024-09-29 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_remove_message_unique_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
