# Generated by Django 4.2.7 on 2023-11-20 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_schedulevaccine_nurse_alter_schedulevaccine_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulevaccine',
            name='schedule_time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 20, 8, 26, 11, 261165, tzinfo=datetime.timezone.utc)),
        ),
    ]
