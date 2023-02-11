import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import geo, Point, Path, Polygon


class geoTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = geo
        fields = ('pk', 'id', 'name', 'actions')
        default_columns = 'name'

class PointTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = Point
        fields = (
            'pk', 'id', 'name', 'description', 'site', 'tenant', 'lat', 'lon'
        )
        default_columns = 'name', 'description', 'site', 'tenant', 'lat', 'lon'

class PathTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Path
        fields = (
            'pk', 'id', 'name', 'description', 'a_site', 'z_site', 'circuit', 'tenant'
        )
        default_columns = 'name', 'description', 'a_site', 'z_site', 'circuit', 'tenant'

class PolygonTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Polygon
        fields = (
            'pk', 'id', 'name', 'description', 'sitegroups', 'regions', 'tenant'
        )
        default_columns = 'name', 'description', 'sitegroups', 'regions', 'tenant'