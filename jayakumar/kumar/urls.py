from .views import flipkartViewSet
from .views import morningViewSet
from .views import adminViewSet
from .views import itemsViewSet
from .views import morningitemsViewSet
from .views import morningfoodViewSet
from .views import morningfoodcartViewSet

from .views import coffeeViewSet
from .views import coffeecartViewSet


from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'flipkart', flipkartViewSet)
router.register(r'morning', morningViewSet)
router.register(r'admin', adminViewSet)
router.register(r'items', itemsViewSet)
router.register(r'morningitems', morningitemsViewSet)
router.register(r'morningfood', morningfoodViewSet)
router.register(r'morningfoodcart', morningfoodcartViewSet)
router.register(r'coffee', coffeeViewSet)
router.register(r'coffeecart', coffeecartViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
