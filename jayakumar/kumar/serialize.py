from .models import flipkart
from .models import morning
from .models import admin
from .models import items
from .models import morningitems
from .models import morningfood
from .models import morningfoodcart
from .models import coffee
from .models import coffeecart


from rest_framework import serializers


class flipkartSerializer(serializers.ModelSerializer):
    class Meta:
        model = flipkart
        fields = ('__all__')


class morningSerializer(serializers.ModelSerializer):
    class Meta:
        model = morning
        fields = ('__all__')


class adminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = ('__all__')


class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ('__all__')


class morningitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = morningitems
        fields = ('__all__')


class morningfoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = morningfood
        fields = ('__all__')


class morningfoodcartSerializer(serializers.ModelSerializer):
    class Meta:
        model = morningfoodcart
        fields = ('__all__')


class coffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffee
        fields = ('__all__')


class coffeecartSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffeecart
        fields = ('__all__')
