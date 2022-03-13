from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api.views import UserViewSet, StudentViewSet, DepartmentEventViewSet, CollegeEventViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('department-events', DepartmentEventViewSet)
router.register('college-events', CollegeEventViewSet)


urlpatterns = [
    path('', include(router.urls)),
]