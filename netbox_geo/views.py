from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class geoView(generic.ObjectView):
    queryset = models.geo.objects.all()


class geoListView(generic.ObjectListView):
    queryset = models.geo.objects.all()
    table = tables.geoTable


class geoEditView(generic.ObjectEditView):
    queryset = models.geo.objects.all()
    form = forms.geoForm


class geoDeleteView(generic.ObjectDeleteView):
    queryset = models.geo.objects.all()


