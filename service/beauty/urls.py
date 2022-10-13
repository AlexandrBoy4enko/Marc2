from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.PersonViewSet)
router.register(r'material', views.MaterialViewSet)
router.register(r'service', views.ServicesViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('api/v1.1/', include(router.urls)),
    # path('api/v1.1/', include('rest_framework.urls', namespace='rest_framework'))
]
