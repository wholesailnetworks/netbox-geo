from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_geo'
router = NetBoxRouter()
router.register('points', views.PointListViewSet)

urlpatterns = router.urls