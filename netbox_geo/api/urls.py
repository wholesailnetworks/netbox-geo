from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_geo'
router = NetBoxRouter()
router.register('point', views.PointListViewSet)
router.register('path', views.PathListViewSet)
router.register('polygon', views.PolygonListViewSet)
urlpatterns = router.urls