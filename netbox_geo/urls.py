from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (

    path('geos/', views.geoListView.as_view(), name='geo_list'),
    path('geos/add/', views.geoEditView.as_view(), name='geo_add'),
    path('geos/<int:pk>/', views.geoView.as_view(), name='geo'),
    path('geos/<int:pk>/edit/', views.geoEditView.as_view(), name='geo_edit'),
    path('geos/<int:pk>/delete/', views.geoDeleteView.as_view(), name='geo_delete'),
    path('geos/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='geo_changelog', kwargs={
        'model': models.geo
    }),
    path('point/', views.pointListView.as_view(), name='point_list'),
    path('point/add/', views.pointEditView.as_view(), name='point_add'),
    path('point/<int:pk>/', views.pointView.as_view(), name='point'),
    path('point/<int:pk>/edit/', views.pointEditView.as_view(), name='point_edit'),
    path('point/<int:pk>/delete/', views.pointDeleteView.as_view(), name='point_delete'),
    path('point/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='point_changelog', kwargs={
        'model': models.Point
    }),

)
