# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponseNotFound,HttpResponse
from .models import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings
from datetime import datetime

def home(request):
	return HttpResponse('Electronic Toll Collection')

@csrf_exempt
def logTollCharge(request):
	
	if request.method != 'POST':
		return HttpResponseNotFound('Invalid Request')
	
	vehicle_rfid = request.POST['vehicle_rfid']
	vehicle_rfid = vehicle_rfid.strip(' ')
	
	if not (vehicle_rfid):
		return HttpResponseNotFound('Insufficient Data')
	
	try:
		vehicle = Vehicle.objects.get(v_rfid=vehicle_rfid)
	except Vehicle.DoesNotExist:
		return HttpResponseNotFound('Vehicle not found')

	amount = VehicleType.objects.get(name = vehicle.v_type).charge

	vehicle.owner.wallet_bal -= int(amount)
	vehicle.owner.save()
	newCharge = TollCharge(vehicle=vehicle, timestamp=datetime.now())
	newCharge.save()

	message = 'Rs.' + str(amount) + ' is deducted from your account during toll cross at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	message += '\nCurrent balance is ' + str(vehicle.owner.wallet_bal)
	settings.EMAIL_HOST_USER
	frmemail = settings.EMAIL_HOST_USER
	toemail = str(vehicle.owner.email)
	#send_mail('Toll Charge', message, frmemail, [toemail], fail_silently=False)
	
	return HttpResponse('Successfully charged Rs.' + str(amount) + ' to ' + str(vehicle))

def logGetReq(request, v_rfid):
	r = requests.post('http://127.0.0.1:8000/log/',proxies={'http':'','https':''}, data = {'vehicle_rfid': v_rfid})
	return HttpResponse(str(r.text))