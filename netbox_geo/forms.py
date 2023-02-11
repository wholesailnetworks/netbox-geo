from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import Point, Path, Polygon
class PointForm(NetBoxModelForm):
    
    class Meta:
        model = Point
        fields = ('name', 'description', 'site', 'tenant', 'lat', 'lon')
        