from django.contrib.gis.geoip2 import GeoIP2

def get_geo_info(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, long = g.lat_lon(ip)
    return country, city, lat, long