# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 21:21
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0026_add_rack_reservations'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='dcim.Site'),
        ),
    ]
