from django.db import transaction, DatabaseError
from django.db.models import F
from django.http import HttpResponse
from pygments.styles import material
from rest_framework import viewsets, mixins
from rest_framework.exceptions import ParseError, MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from beauty.api.domain_layer.serialization.serializers import OrdersSerializer, OrderUpdateSerializer, \
    CreateOrderSerializer, UpdateOrderSerializer
from beauty.api.core.models.models import Order, Membership, Material, Services


class OrderViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet,
                   ):
    queryset = Order.objects.all()

    _serializers = {
        "POST": CreateOrderSerializer,
        "PUT": UpdateOrderSerializer,
        "GET": OrdersSerializer,
    }

    def get_serializer_class(self):
        return self._serializers.get(self.request.method)

    def get_queryset(self):
        queryset = super().get_queryset()
        profit = self.request.query_params.get('profit', None)
        if profit is not None:
            queryset = queryset.filter(profit=F('profit')-F('uuid_service__price'))
        return queryset

    def create(self, request, *args, **kwargs):
        return self.create_or_update(request)

    def put(self, request, *args, **kwargs):
        return self.create_or_update(request)

    def create_or_update(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data  # type: dict

        order = self._create_or_update(validated_data)
        order_serializer = OrdersSerializer(order)

        return Response(data=order_serializer.data, status=200)

    def _create_or_update(self, validated_data):
        with transaction.atomic():
            try:
                try:
                    order = Order.objects.get(
                        uuid=validated_data["uuid"],
                    )
                except (DatabaseError, KeyError):
                    order = Order.objects.create(
                        date_time=validated_data["date_time"],
                        profit=0,
                    )

                order.uuid_person_id = validated_data["uuid_person"]
                order.uuid_service_id = validated_data["uuid_service"]

                current_materials = Membership.objects.filter(uuid_order_id=order.uuid).all()
                current_materials.delete()

                profit = 0
                for material in validated_data["materials"]:
                    Membership.objects.create(
                        uuid_order_id=order.uuid,
                        uuid_material_id=material["uuid"],
                    )
                    material_instance = Material.objects.get(uuid=material["uuid"])
                    profit += material["count"] * material_instance.price

                service = Services.objects.get(uuid=validated_data["uuid_service"])
                order.profit = profit + service.price
                order.save()

            except (DatabaseError, TypeError, KeyError) as error:
                raise ParseError(detail=str(error))
        return order

    def perform_destroy(self, order):
        with transaction.atomic():
            try:
                current_materials = Membership.objects.filter(uuid_order_id=order.uuid).all()
                current_materials.delete()

                order.delete()
            except Exception as error:
                print(error)
                raise ParseError(detail=str(error))
