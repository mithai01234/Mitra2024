# Generated by Django 4.1.13 on 2024-05-06 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0005_alter_statusapp_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusapp',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 11, 58, 17, 490743, tzinfo=datetime.timezone.utc)),
        ),
    ]
