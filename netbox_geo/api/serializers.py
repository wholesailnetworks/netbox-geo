from rest_framework_gis import serializers as gis_serializers
from rest_framework import serializers
from django.core.serializers import serialize
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Point, Path, Polygon

class NestedAccessListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_geo-api:point-detail'
    )

    class Meta:
        model = Point
        fields = ('id', 'url', 'display', 'name') 
class PointSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_geo-api:point-detail'
    )
    
    class Meta:
        model = Point
        fields = ('id', 'url', 'display', 'name', 'point', 'description', 'site', 'tenant', 'lat', 'lon', 'tags', 'custom_fields', 'created', 'last_updated',)
class PathSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_geo-api:path-detail'
    )
    class Meta:
        model = Path
        fields = ('id', 'url', 'display', 'name', 'description', 'a_site', 'z_site', 'circuit', 'tenant', 'path', 'tags', 'custom_fields', 'created', 'last_updated',)

class PolygonSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_geo-api:polygon-detail'
    )
    class Meta:
        model = Polygon
        fields = ('id', 'url', 'display', 'name', 'description', 'sitegroups', 'regions', 'tenant', 'polygon', 'tags', 'custom_fields', 'created', 'last_updated',)
