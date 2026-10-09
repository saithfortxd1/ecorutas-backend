from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Categoria, Experiencia, Disponibilidad
from .serializers import CategoriaSerializer, ExperienciaSerializer, DisponibilidadSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer
    # Implementación básica de Búsqueda y Filtros (RF-03)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'descripcion', 'categoria__nombre']
    ordering_fields = ['precio_unitario', 'created_at']

class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer