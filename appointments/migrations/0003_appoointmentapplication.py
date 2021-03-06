# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20170416_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppoointmentApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('app_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='appointments.Appointment_Date', verbose_name='dates')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='appointments.Appointment', verbose_name='appointment')),
            ],
            options={
                'verbose_name_plural': 'Appointment Applications',
                'verbose_name': 'Appointment Application',
            },
        ),
    ]
