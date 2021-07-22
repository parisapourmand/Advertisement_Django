# Generated by Django 3.2.5 on 2021-07-22 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertiser_management', '0008_auto_20210722_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='highlighted',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL),
        ),
    ]