# Generated by Django 4.2.7 on 2023-11-18 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usermodel_age_alter_usermodel_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.ImageField(blank=True, null=True, upload_to='ssn/')),
                ('race', models.CharField(blank=True, max_length=225, null=True)),
                ('occupaon', models.CharField(blank=True, max_length=225, null=True)),
                ('medical_history', models.TextField(blank=True, max_length=1500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
