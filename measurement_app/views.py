from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo_info
from django.template import RequestContext
import folium
def calculateDistanceView(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geoLocator = Nominatim(user_agent='measurement_app')
    # ip = '72.14.207.99'
    # country, city, lat, long = get_geo_info(ip)
    # #print('location country - ', country)
    # #print('location city - ', city)
    # #print('location lat - ', lat)
    # #print('location long - ', long)

    # location = geoLocator.geocode(city)
    # print('location - ', location)
    # # loc_lat = lat
    # # loc_long = long
    # # pointA = (loc_lat, loc_long)
    m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

    if form.is_valid():
        instance = form.save(commit=False)    
        
        destination_form = form.cleaned_data.get('destination')
        destination = geoLocator.geocode(destination_form)

        location_form = form.cleaned_data.get('location')
       
        # print(destination)
        location = geoLocator.geocode(location_form)
        print('this is loc - ', location)

        location_lat = location.latitude
        location_long = location.longitude
        pointA = (location_lat, location_long)
        print('this is point a - ', location_lat)
        # mapFolium = folium.map(width=800, height=500, location=pointA)
        destination_lat = destination.latitude
        destination_long = destination.longitude

        pointB = (destination_lat, destination_long)
        distance = round(geodesic(pointA, pointB).km,2)
        instance.destination = form.cleaned_data.get('destination')
        instance.location= location
        instance.distance = distance
        instance.save()
        folium.Marker(location=pointA).add_to(m)
        folium.Marker(location=pointB).add_to(m)
    m = m._repr_html_()
    context = {
        'distance': obj,
        'form': form,
        'map': m,
    }

    return render(request, 'measurement_app/main.html', context)
