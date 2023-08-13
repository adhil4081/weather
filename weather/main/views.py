from django.shortcuts import render
from datetime import datetime
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST.get('location')
        city=city.upper()
       

        date=datetime.now()
        res=urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q='+city+'&appid=7eff708e8473bda5a03a0064c43a656b').read()
        json_data=json.loads(res)
        cord={
            "long": str(json_data[0]['lon']),
            "lat": str(json_data[0]['lat'])
            
        }
        lon=cord['long']
        lat=cord['lat']
        res1=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=7eff708e8473bda5a03a0064c43a656b').read()
        json_data1=json.loads(res1)
        raindata=json_data1.get('rain',{})
        data={
        "country_code": str(json_data1['sys']['country']),
        'clouds':str(json_data1['clouds']['all']),
        'humidity':str(json_data1['main']['humidity']),
        'wind':str(json_data1['wind']['speed']),
        'rain':str(raindata.get('3h','')),
        'weather_icon':str(json_data1['weather'][0]['icon']),
        'temp':int(json_data1['main']['temp']-273.15)
      

        }
        icon_src='https://openweathermap.org/img/wn/'+data['weather_icon']+'@2x.png'
        
    else:
        city = ''
        date =''
        data={}
        cord={}
        icon_src=''
    return render(request, "index.html", {'city': city,'date':date,'cord':cord,'data':data,'icon_src':icon_src})
