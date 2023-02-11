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
