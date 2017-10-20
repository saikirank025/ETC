# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TollUser, Vehicle, TollCharge, VehicleType

admin.site.register(TollUser)
admin.site.register(Vehicle)
admin.site.register(TollCharge)
admin.site.register(VehicleType)