# Generated by Django 4.0.2 on 2022-03-27 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0005_remove_assets_accumulated_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assets',
            name='historical_cost',
        ),
    ]