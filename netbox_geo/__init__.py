"""Top-level package for NetBox Geospatial Plugin."""

__author__ = """Wholesail Networks"""
__email__ = 'nick.bogle@ziply.com'
__version__ = '0.1.0'


from extras.plugins import PluginConfig


class geoConfig(PluginConfig):
    name = 'netbox_geo'
    verbose_name = 'NetBox Geospatial Plugin'
    description = 'Netbox GeoDjango Plugin for visualizing sites, cables, circuits, etc.'
    version = 'version'
    base_url = 'netbox_geo'
    django_apps = ["django.contrib.gis"] 

config = geoConfig