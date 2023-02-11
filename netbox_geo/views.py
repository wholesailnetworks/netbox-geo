from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PathForm

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
    def upload_file(request):
        if request.method == 'POST':
            form = PathForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = PathForm()
        return render(request, 'upload.html', {'form': form})

class pathListView(generic.ObjectListView):
    queryset = models.Path.objects.all()
    table = tables.PathTable

class pathEditView(generic.ObjectEditView):
    queryset = models.Path.objects.all()
    form = forms.PathForm

class pathDeleteView(generic.ObjectDeleteView):
    queryset = models.Path.objects.all()

class polygonView(generic.ObjectView):
    queryset = models.Polygon.objects.all()

class polygonListView(generic.ObjectListView):
    queryset = models.Polygon.objects.all()
    table = tables.PolygonTable

class polygonEditView(generic.ObjectEditView):
    queryset = models.Polygon.objects.all()
    form = forms.PolygonForm

class polygonDeleteView(generic.ObjectDeleteView):
    queryset = models.Polygon.objects.all()