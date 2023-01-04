from django.urls import path, include
from rest_framework import routers
from tareas.api.views import TareaViewSet

router = routers.DefaultRouter()
router.register("tareas", TareaViewSet, basename="tarea.api.viewset")


urlpatterns = [
    path("", include(router.urls)),
]
