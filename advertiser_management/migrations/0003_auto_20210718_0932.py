# Generated by Django 3.2.5 on 2021-07-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0002_auto_20210718_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='click',
            name='ipaddress',
            field=models.GenericIPAddressField(default='000.000.0.0'),
        ),
        migrations.AddField(
            model_name='view',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='view',
            name='ipaddress',
            field=models.GenericIPAddressField(default='000.000.0.0'),
        ),
    ]