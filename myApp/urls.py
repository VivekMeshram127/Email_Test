from . import views
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet, EventViewSet, EmailTemplateViewSet


router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'events', EventViewSet)
router.register(r'emailtemplates', EmailTemplateViewSet)


urlpatterns = [

    path("", views.home , name="home"),
    path('api/', include(router.urls)),

]

