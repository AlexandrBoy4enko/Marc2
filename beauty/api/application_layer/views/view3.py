from rest_framework import viewsets

from beauty.api.domain_layer.serialization.serializers import ServicesSerializer
from beauty.api.core.models.models import Services


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer