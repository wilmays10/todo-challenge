from datetime import datetime
from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import ValidationError
from tareas.models import Tarea
from tareas.api.serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    """
    Muestra todas las tareas.
    Se puede buscar por los campos titulo o descripcion.
    Se puede filtrar por fecha de creación: formato YYYY-m-d.
    Por ejemplo: fecha=2023-1-15
    """

    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["titulo", "descripcion"]

    def get_queryset(self):
        queryset = Tarea.objects.all()
        fecha = self.request.query_params.get("fecha", None)
        if fecha is not None:
            try:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError(detail="Formato de fecha invalido.")
            queryset = queryset.filter(timestamp=fecha)

        return queryset
