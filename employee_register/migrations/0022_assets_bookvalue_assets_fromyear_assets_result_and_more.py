# Generated by Django 4.0.2 on 2022-03-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0021_remove_assets_bookvalue_remove_assets_from_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='bookValue',
            field=models.DecimalField(decimal_places=2, default=2500, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='fromYear',
            field=models.IntegerField(default=2021),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='result',
            field=models.DecimalField(decimal_places=2, default=1500, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='service',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
