# Generated by Django 4.2.7 on 2023-11-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_alter_schedulevaccine_schedule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulevaccine',
            name='schedule_time',
            field=models.TimeField(),
        ),
    ]
