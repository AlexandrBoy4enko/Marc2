from datetime import datetime
from typing import List

from django.db import transaction, DatabaseError
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.fields import IntegerField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import Serializer, ListSerializer

from beauty.api.core.models.models import Person, Material, Services, Order, CategoryPerson


class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CategoryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPerson
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    def validate_price(self, value):
        try:
            Material.objects.get(price=value)
        except Material.DoesNotExist:
            raise NotFound(detail={"message": "Material должен быть числом"})
        return value


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # uuid_person = serializers.CharField(source="uuid_person.name")
    uuid_materials = MaterialsSerializer(many=True)
    uuid_service = ServicesSerializer()


class NestedMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            "uuid",
            # "count",
        )

    # count = IntegerField(min_value=0)


class NewMaterialsSerializer(IntegerField):
    def to_internal_value(self, data):
        pk = super().to_internal_value(data)
        try:
            Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            raise NotFound(detail={"message": "Материал с таким uuid не существует."})
        return pk


class TestSerializer(Serializer):
    uuid = NewMaterialsSerializer()
    count = IntegerField(min_value=0)


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'uuid',
            'uuid_person',
            'uuid_service',
            'materials',
            'date_time',
        )

    materials = ListSerializer(child=TestSerializer())

    def create(self, validated_data):
        with transaction.atomic():
            try:
                order = Order.objects.create(
                    uuid_person_id=validated_data["uuid_person"],
                    profit=self._get_profit_value(validated_data),
                    uuid_service_id=validated_data["uuid_service"],
                    date_time=validated_data["date_time"],
                )
                # order.uuid_materials.add(*validated_data["materials"])
                # order.uuid_service.add(*validated_data["uuid_service"])
            except DatabaseError:
                return HttpResponse(status=500)
        return order

    def _get_profit_value(self, validated_data):
        materials = validated_data["materials"]
        materials_price = sum((Material.objects.get(pk=obj['uuid']).price * obj['count'] for obj in materials))
        return materials_price


class MaterialForCreateOrderSerializer(Serializer):
    uuid = IntegerField(min_value=-2)
    count = IntegerField(min_value=-3)


class CreateOrderSerializer(serializers.Serializer):
    uuid_person = serializers.IntegerField(min_value=0)
    uuid_service = serializers.IntegerField(min_value=-1)
    date_time = serializers.DateField()
    materials = serializers.ListSerializer(child=MaterialForCreateOrderSerializer())

    def validate_uuid_person(self, value):
        try:
            return Person.objects.get(uuid=value)
        except:
            raise ParseError(detail={"Person": f"Instance with id {value} not found"})

    def validate_uuid_service(self, value):
        try:
            Services.objects.get(uuid=value)
        except Services.DoesNotExist:
            raise NotFound(detail={"message": "Services с таким uuid не существует."})
        return value

    def validate_materials(self, values: List[dict]):
        try:
            [Material.objects.get(uuid=value["uuid"]) for value in values]
        except Material.DoesNotExist:
            raise NotFound(detail={"message": "Material с таким uuid не существует."})
        return values


class UpdateOrderSerializer(CreateOrderSerializer):
    uuid = IntegerField(min_value=0)

    def validate_uuid(self, value):
        try:
            Order.objects.get(uuid=value)
        except Order.DoesNotExist:
            raise NotFound(detail={"message": "Order с таким uuid не существует."})
        return value
