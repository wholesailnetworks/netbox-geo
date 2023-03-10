# Generated by Django 4.1.6 on 2023-02-11 19:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0009_standardize_description_comments'),
        ('circuits', '0041_standardize_description_comments'),
        ('dcim', '0167_module_status'),
        ('extras', '0084_staging'),
        ('netbox_geo', '0003_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polygons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('regions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.region')),
                ('sitegroups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.sitegroup')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant')),
            ],
            options={
                'verbose_name': 'Polygons',
                'verbose_name_plural': 'Polygons',
            },
        ),
        migrations.CreateModel(
            name='Paths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('path', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('a_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_a_related', to='dcim.site')),
                ('circuit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='circuits.circuit')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant')),
                ('z_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_z_related', to='dcim.site')),
            ],
            options={
                'verbose_name': 'Paths',
                'verbose_name_plural': 'Paths',
            },
        ),
    ]
