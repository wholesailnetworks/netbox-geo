from rest_framework import serializers

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