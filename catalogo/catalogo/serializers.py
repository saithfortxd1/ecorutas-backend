from rest_framework import serializers
from .models import Categoria, Experiencia, ExperienciaTraduccion, FotoExperiencia, Disponibilidad

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ExperienciaTraduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaTraduccion
        fields = ['id', 'idioma', 'titulo_traducido', 'descripcion_traducida']

class FotoExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoExperiencia
        fields = ['id', 'url_foto', 'es_principal']

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class ExperienciaSerializer(serializers.ModelSerializer):
    # Relaciones anidadas (Filtro entre tablas)
    traducciones = ExperienciaTraduccionSerializer(many=True, read_only=True)
    fotos = FotoExperienciaSerializer(many=True, read_only=True)
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Experiencia
        fields = [
            'id', 'anfitrion', 'categoria', 'categoria_nombre', 'titulo',
            'descripcion', 'precio_unitario', 'latitud', 'longitud',
            'estado', 'created_at', 'traducciones', 'fotos'
        ]