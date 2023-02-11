from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables

class pointView(generic.ObjectView):
    queryset = models.Point.objects.all()

class pointListView(generic.ObjectListView):
    queryset = models.Point.objects.all()
    table = tables.PointTable

class pointEditView(generic.ObjectEditView):
    queryset = models.Point.objects.all()
    form = forms.PointForm

class pointDeleteView(generic.ObjectDeleteView):
    queryset = models.Point.objects.all()

class pathView(generic.ObjectView):
    queryset = models.Path.objects.all()

class pathListView(generic.ObjectListView):
    queryset = models.Path.objects.all()
    table = tables.PointTable

class pathEditView(generic.ObjectEditView):
    queryset = models.Path.objects.all()
    form = forms.PointForm

class pathDeleteView(generic.ObjectDeleteView):
    queryset = models.Path.objects.all()

class polygonView(generic.ObjectView):
    queryset = models.Polygon.objects.all()

class polygonListView(generic.ObjectListView):
    queryset = models.Polygon.objects.all()
    table = tables.PointTable

class polygonEditView(generic.ObjectEditView):
    queryset = models.Polygon.objects.all()
    form = forms.PointForm

class polygonDeleteView(generic.ObjectDeleteView):
    queryset = models.Polygon.objects.all()