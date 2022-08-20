# Generated by Django 4.0.5 on 2022-08-20 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_rename_regedter_mesaage_regester_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mesaage',
            options={'managed': True, 'verbose_name': 'پیام', 'verbose_name_plural': 'پیام'},
        ),
        migrations.AlterField(
            model_name='places',
            name='regeste',
            field=models.DateField(default=datetime.datetime(2022, 8, 20, 8, 57, 23, 76218, tzinfo=utc), verbose_name='تاریخ ثبت'),
        ),
    ]
