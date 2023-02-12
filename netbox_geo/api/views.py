from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import PathSerializer, PointSerializer, PolygonSerializer

class PointListViewSet(NetBoxModelViewSet):
    queryset = models.Point.objects.prefetch_related()
    serializer_class = PointSerializer
    
class PathListViewSet(NetBoxModelViewSet):
    queryset = models.Path.objects.prefetch_related()
    serializer_class = PathSerializer
    
class PolygonListViewSet(NetBoxModelViewSet):
    queryset = models.Polygon.objects.prefetch_related()
    serializer_class = PolygonSerializer