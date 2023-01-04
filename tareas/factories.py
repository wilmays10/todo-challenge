import factory
from tareas.models import Tarea


class TareaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tarea

    titulo = factory.Sequence(lambda n: 'titulo%d' % n)
    descripcion = factory.Sequence(lambda n: 'descripcion%d' % n)
    comentario = factory.Sequence(lambda n: 'comentario%d' % n)
    completada = False
