from django.db import models
from django.urls import reverse
from django.contrib.gis.db import models

from netbox.models import NetBoxModel


class geo(NetBoxModel):
    name = models.CharField(
        max_length=100
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:geo', args=[self.pk])

class Point(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        blank=True,
        null=True
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    lon = models.FloatField()
    lat = models.FloatField()
    point = models.PointField()
    class Meta:
        verbose_name = 'Points'
        verbose_name_plural = 'Points'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:geo', args=[self.pk])

    def clean(self):
        super().clean()

# class Paths(models.Model):
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()

#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name