from rest_framework import routers
from beauty.api.application_layer.views import view1, view2, view3, view4, view5

router = routers.DefaultRouter()
router.register(r'user', view1.PersonViewSet)
router.register(r'material', view2.MaterialViewSet)
router.register(r'service', view3.ServicesViewSet)
router.register(r'order', view4.OrderViewSet)
router.register(r'category', view5.CategoryPersonViewSet)

urlpatterns = router.urls
