# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TollUser, Vehicle, TollCharge, VehicleType

class TollUserAdmin(admin.ModelAdmin):
	list_display = ('name','phone','email','wallet_bal')

class VehicleAdmin(admin.ModelAdmin):
	list_display = ('v_number','v_rfid','owner','v_type')

class TollChargeAdmin(admin.ModelAdmin):
	list_display = ('vehicle', 'timestamp')

class VehicleTypeAdmin(admin.ModelAdmin):
	list_display = ('name','charge')



admin.site.register(TollUser, TollUserAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(TollCharge, TollChargeAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)