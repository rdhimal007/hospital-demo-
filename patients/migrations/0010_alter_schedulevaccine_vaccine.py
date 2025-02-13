# Generated by Django 4.2.7 on 2023-11-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccines', '0004_rename_stock_vaccine_available'),
        ('patients', '0009_schedulevaccine_on_holding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulevaccine',
            name='vaccine',
            field=models.ForeignKey(blank=True, limit_choices_to={'availability': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccines.vaccine'),
        ),
    ]
