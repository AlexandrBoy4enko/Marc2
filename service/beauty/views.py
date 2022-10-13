from rest_framework import viewsets
from beauty.models import Person, Material, Services, Order
from beauty.serializers import PersonsSerializer, MaterialsSerializer, ServicesSerializer, OrdersSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonsSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialsSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
