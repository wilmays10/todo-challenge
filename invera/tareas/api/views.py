from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from tareas.models import Tarea
from tareas.api.serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Tarea.objects.all()
