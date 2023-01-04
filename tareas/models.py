from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=90)
    descripcion = models.TextField()
    comentario = models.CharField(max_length=250, blank=True, null=True)
    completada = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.titulo}"
