from rest_framework import viewsets

from beauty.api.domain_layer.serialization.serializers import CategoryPersonSerializer
from beauty.api.core.models.models import CategoryPerson


class CategoryPersonViewSet(viewsets.ModelViewSet):
    queryset = CategoryPerson.objects.all()
    serializer_class = CategoryPersonSerializer
