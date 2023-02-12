from django.contrib.gis.geos import Point
from django.contrib.gis.geos import LineString
from django.contrib.gis.measure import Distance, D
from shapely.wkt import loads

def length_calc(path):
    points = []
    for lat,lon in path.path.coords:
        pnt = Point(float(lon), float(lat))
        points.append(pnt)
    track.length = Track.objects.length().get(id=track.id).length.km
    track.save()