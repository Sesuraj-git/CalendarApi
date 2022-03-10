from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]