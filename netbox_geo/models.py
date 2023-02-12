from django.db import models
from django.urls import reverse
from django.contrib.gis.db import models

from netbox.models import NetBoxModel


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
    point = models.PointField(
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = 'Point'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:point', args=[self.pk])

    def clean(self):
        super().clean()

class Path(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    a_site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name="%(class)s_a_related",
        blank=True,
        null=True
    )
    z_site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name="%(class)s_z_related",
        blank=True,
        null=True
    )
    circuit = models.ForeignKey(
        to='circuits.Circuit',
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
    path = models.LineStringField(
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Path'
        verbose_name_plural = 'Path'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:path', args=[self.pk])

    def clean(self):
        super().clean()
        
class Polygon(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    sitegroups = models.ForeignKey(
        to='dcim.SiteGroup',
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        blank=True,
        null=True
    )
    regions = models.ForeignKey(
        to='dcim.Region',
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
    polygon = models.PolygonField(
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Polygon'
        verbose_name_plural = 'Polygon'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:polygon', args=[self.pk])

    def clean(self):
        super().clean()