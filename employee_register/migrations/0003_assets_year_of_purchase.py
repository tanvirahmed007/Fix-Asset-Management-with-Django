# Generated by Django 4.0.2 on 2022-03-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_rename_employee_assets'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='year_of_purchase',
            field=models.IntegerField(default=2022),
            preserve_default=False,
        ),
    ]
