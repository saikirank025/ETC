from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^log/(?P<v_rfid>[a-zA-Z0-9]+)$', logGetReq),
    url(r'^log/$', logTollCharge),
]
