# Generated by Django 2.0 on 2017-12-24 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171224_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_price',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
