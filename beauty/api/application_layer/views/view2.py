from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from beauty.api.domain_layer.serialization.serializers import MaterialsSerializer
from beauty.api.core.models.models import Material


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        price = self.request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(price=price)
        return queryset
        # ordering = self.request.query_params.get('ordering', None)
        # if ordering is not None:
        #     queryset = queryset.order_by(ordering)
        # return queryset
