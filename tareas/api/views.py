from rest_framework import viewsets, permissions
from tareas.models import Tarea
from tareas.api.serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarea.objects.all()
