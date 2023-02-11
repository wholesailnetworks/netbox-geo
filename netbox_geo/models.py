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
        return reverse('plugins:netbox_geo:points', args=[self.pk])

    def clean(self):
        super().clean()

class Paths(NetBoxModel):
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
    path = models.LineStringField()
    class Meta:
        verbose_name = 'Paths'
        verbose_name_plural = 'Paths'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:paths', args=[self.pk])

    def clean(self):
        super().clean()
        
class Polygons(NetBoxModel):
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
    polygon = models.PolygonField()
    class Meta:
        verbose_name = 'Polygons'
        verbose_name_plural = 'Polygons'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_geo:polygons', args=[self.pk])

    def clean(self):
        super().clean()