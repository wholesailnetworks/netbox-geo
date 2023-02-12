from extras.plugins import PluginTemplateExtension
from django.db.models import Q
from .models import Path, Point, Polygon

class PointList(PluginTemplateExtension):
    model = 'dcim.site'
    def left_page(self):
        return self.render('netbox_geo/point_include.html', extra_context={
            'points': Point.objects.filter(site=self.context['object'])
        })
        
template_extensions = [PointList]