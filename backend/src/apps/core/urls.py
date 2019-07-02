from django.urls import path
from .views import OrderViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/all', OrderViewSet, 'all')


urlpatterns = router.urls
