# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

positionchoices = (
    ('Admin' ,'Admin'),
    ('User', 'User')
    )
vehiclechoices = (
	('Car', 'Car'),
	('Bus', 'Bus'),
	('Auto', 'Auto')
	)

class VehicleType(models.Model):
	name = models.CharField(max_length = 300, choices = vehiclechoices)
	charge = models.IntegerField()

	def __unicode__(self):
		return self.name

class TollUser(models.Model):
	name = models.CharField(max_length = 300,default='',blank=False,null=False)
	position = models.CharField(max_length=300,choices = positionchoices, blank=False,null=False)
	email = models.CharField(max_length = 300,default='#')
	phone = models.CharField(max_length = 15,default='#')
	wallet_bal = models.IntegerField(default=0,null=False)

	def __unicode__(self):
		return self.name

class Vehicle(models.Model):
	v_number = models.CharField(max_length = 20,default='',blank=False,null=False)
	v_type = models.CharField(max_length=300,choices = vehiclechoices, blank=False,null=False)
	owner = models.ForeignKey(TollUser)
	v_rfid = models.CharField(max_length=30,default='#', blank=False,null=False)

	def __unicode__(self):
		return self.owner.name + '\'s ' + self.v_type + ' ' + self.v_number

class TollCharge(models.Model):
	vehicle = models.ForeignKey(Vehicle)
	timestamp = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.vehicle) + ' at ' + str(self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))