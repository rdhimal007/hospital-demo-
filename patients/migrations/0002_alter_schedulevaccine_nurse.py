# Generated by Django 4.2.7 on 2023-11-20 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulevaccine',
            name='nurse',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_nurse': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
