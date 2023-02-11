from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import geo


class geoForm(NetBoxModelForm):

    class Meta:
        model = geo
        fields = ('name', 'tags')
