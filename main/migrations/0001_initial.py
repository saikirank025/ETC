# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TollCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TollUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('position', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=300)),
                ('email', models.CharField(default='#', max_length=300)),
                ('phone', models.CharField(default='#', max_length=15)),
                ('wallet_bal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_number', models.CharField(default='', max_length=20)),
                ('v_type', models.CharField(choices=[('Car', 'Car'), ('Bike', 'Bike'), ('Bus', 'Bus'), ('Auto', 'Auto')], max_length=300)),
                ('v_rfid', models.CharField(default='#', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TollUser')),
            ],
        ),
        migrations.AddField(
            model_name='tollcharge',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vehicle'),
        ),
    ]
