# Generated by Django 4.0.2 on 2022-03-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0017_assets_mainvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='bookValue',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='from_year',
            field=models.IntegerField(default=2021),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='service_year',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
