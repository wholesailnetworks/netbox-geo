from django import forms
from django.contrib.gis import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from django.db import models
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import Point, Path, Polygon

class PointForm(NetBoxModelForm):
    # point = forms.PointField(widget=
    #     forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    class Meta:
        model = Point
        fields = ('name', 'description', 'point','site', 'tenant', 'lat', 'lon')

class PathForm(NetBoxModelForm):
    class Meta:
        model = Path
        fields = ('name', 'description', 'a_site', 'z_site', 'circuit', 'tenant')
        
class PolygonForm(NetBoxModelForm):
    
    class Meta:
        model = Polygon
        fields = ('name', 'description', 'sitegroups', 'regions', 'tenant')
        
class PointFilterForm(NetBoxModelFilterSetForm):
    model = Point
