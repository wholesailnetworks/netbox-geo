from netbox.filtersets import NetBoxModelFilterSet
from .models import Path, Point, Polygon


# class geoFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = geo
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)

class PointFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = Point
        fields = ('id','name', 'description', 'site', 'tenant', 'lat', 'lon')
        
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
    
class PathFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = Path
        fields = ('id', 'name', 'description', 'a_site', 'z_site', 'circuit', 'tenant')
        
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
class PolygonFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = Polygon
        fields = ('id', 'name', 'description', 'sitegroups', 'regions', 'tenant')
        
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)