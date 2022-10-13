from rest_framework import serializers
from beauty.models import Person, Material, Services, Order


class PersonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'mail')


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
