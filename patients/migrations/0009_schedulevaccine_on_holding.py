# Generated by Django 4.2.7 on 2023-11-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_rename_schedule_schedulevaccine_schedule_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulevaccine',
            name='on_holding',
            field=models.BooleanField(default=True),
        ),
    ]
