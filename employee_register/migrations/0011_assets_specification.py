# Generated by Django 4.0.2 on 2022-03-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0010_assets_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='specification',
            field=models.CharField(default=23, max_length=500),
            preserve_default=False,
        ),
    ]
