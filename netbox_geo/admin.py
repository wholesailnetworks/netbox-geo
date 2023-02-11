from django.contrib import admin
from django.contrib.gis import admin
from .models import Polygon, Path, Point

admin.site.register(Polygon, admin.ModelAdmin)
admin.site.register(Path, admin.ModelAdmin)
admin.site.register(Point, admin.ModelAdmin)