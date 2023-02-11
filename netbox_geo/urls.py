from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (

    path('point/', views.pointListView.as_view(), name='point_list'),
    path('point/add/', views.pointEditView.as_view(), name='point_add'),
    path('point/<int:pk>/', views.pointView.as_view(), name='point'),
    path('point/<int:pk>/edit/', views.pointEditView.as_view(), name='point_edit'),
    path('point/<int:pk>/delete/', views.pointDeleteView.as_view(), name='point_delete'),
    path('point/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='point_changelog', kwargs={
        'model': models.Point
    }),
    path('path/', views.pathListView.as_view(), name='path_list'),
    path('path/add/', views.pathEditView.as_view(), name='path_add'),
    path('path/<int:pk>/', views.pathView.as_view(), name='path'),
    path('path/<int:pk>/edit/', views.pathEditView.as_view(), name='path_edit'),
    path('path/<int:pk>/delete/', views.pathDeleteView.as_view(), name='path_delete'),
    path('path/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='path_changelog', kwargs={
        'model': models.Path
    }),
    path('polygon/', views.polygonListView.as_view(), name='polygon_list'),
    path('polygon/add/', views.polygonEditView.as_view(), name='polygon_add'),
    path('polygon/<int:pk>/', views.polygonView.as_view(), name='polygon'),
    path('polygon/<int:pk>/edit/', views.polygonEditView.as_view(), name='polygon_edit'),
    path('polygon/<int:pk>/delete/', views.polygonDeleteView.as_view(), name='polygon_delete'),
    path('polygon/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='polygon_changelog', kwargs={
        'model': models.Polygon
    }),
    

)
