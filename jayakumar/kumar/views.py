from rest_framework import viewsets
from .serialize import flipkartSerializer
from .models import flipkart

from .serialize import morningSerializer
from .models import morning


from .serialize import adminSerializer
from .models import admin

from .serialize import itemsSerializer
from .models import items

from .serialize import morningitemsSerializer
from .models import morningitems

from .serialize import morningfoodSerializer
from .models import morningfood


from .serialize import morningfoodcartSerializer
from .models import morningfoodcart

from .serialize import coffeeSerializer
from .models import coffee

from .serialize import coffeecartSerializer
from .models import coffeecart


class flipkartViewSet(viewsets.ModelViewSet):
    queryset = flipkart.objects.all()
    serializer_class = flipkartSerializer


class morningViewSet(viewsets.ModelViewSet):
    queryset = morning.objects.all()
    serializer_class = morningSerializer


class adminViewSet(viewsets.ModelViewSet):
    queryset = admin.objects.all()
    serializer_class = adminSerializer


class itemsViewSet(viewsets.ModelViewSet):
    queryset = items.objects.all()
    serializer_class = itemsSerializer


class morningitemsViewSet(viewsets.ModelViewSet):
    queryset = morningitems.objects.all()
    serializer_class = morningitemsSerializer


class morningfoodViewSet(viewsets.ModelViewSet):
    queryset = morningfood.objects.all()
    serializer_class = morningfoodSerializer


class morningfoodcartViewSet(viewsets.ModelViewSet):
    queryset = morningfoodcart.objects.all()
    serializer_class = morningfoodcartSerializer


class coffeeViewSet(viewsets.ModelViewSet):
    queryset = coffee.objects.all()
    serializer_class = coffeeSerializer


class coffeecartViewSet(viewsets.ModelViewSet):
    queryset = coffeecart.objects.all()
    serializer_class = coffeecartSerializer

# Create your views here.
