from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    if request.POST.get('country'):
        if request.POST.get('city'):
            city = request.POST.get('city')
            country = request.POST.get('country')
            url = 'http://api.openweathermap.org/geo/1.0/direct?q=' + city + ',' + country + '&limit=5&appid=39fec22e554397a64fe5d8da88a34d70'
            returnData = requests.get(url).json()
            context = {
                "data":returnData
            }
            template = loader.get_template('city.html')
            return HttpResponse(template.render(context,request))
        elif request.POST.get('zip'):
            zip = request.POST.get('zip')
            country = request.POST.get('country')
            url = 'http://api.openweathermap.org/geo/1.0/zip?zip='+zip+','+country+'&appid=39fec22e554397a64fe5d8da88a34d70'
            returnData = requests.get(url).json()
            context = {
                "data":returnData
            }
            template = loader.get_template('city.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('city.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

def currentWeather(request, lat=0, lon=0):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=39fec22e554397a64fe5d8da88a34d70&units=imperial'
    returnData = requests.get(url).json()
    weather = returnData['main']
    context = {
        'lat':lat,
        'lon':lon,
        'data':returnData,
        'weather':weather,
    }
    template = loader.get_template('current.html')
    return HttpResponse(template.render(context, request))