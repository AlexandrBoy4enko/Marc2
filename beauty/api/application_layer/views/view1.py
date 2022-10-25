from rest_framework import viewsets
from beauty.api.core.models.models import Person
from beauty.api.domain_layer.serialization.serializers import PersonsSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonsSerializer
