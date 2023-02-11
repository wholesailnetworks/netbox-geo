from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import Point, Path, Polygon
class PointForm(NetBoxModelForm):
    
    class Meta:
        model = Point
        fields = ('name', 'description', 'site', 'tenant', 'lat', 'lon')

class PathForm(NetBoxModelForm):
    
    class Meta:
        model = Path
        fields = ('name', 'description', 'a_site', 'z_site', 'circuit', 'tenant')
        
class PolygonForm(NetBoxModelForm):
    
    class Meta:
        model = Polygon
        fields = ('name', 'description', 'sitegroups', 'regions', 'tenant')