from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import PointSerializer

class PointListViewSet(NetBoxModelViewSet):
    queryset = models.Point.objects.prefetch_related()
    serializer_class = PointSerializer