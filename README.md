# EcoRutas Backend

Backend API para la aplicación EcoRutas, construida con Django y Django REST Framework.

## Tecnologías

- Python 3.x
- Django 6.1.2
- Django REST Framework 3.18.3
- drf-yasg (Documentación Swagger)

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd ecorutas-backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración

1. Ejecuta las migraciones:
   ```bash
   python manage.py migrate
   ```
2. Crea un superusuario (opcional):
   ```bash
   python manage.py createsuperuser
   ```

## Ejecución

```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000/`

## Documentación API

- Swagger UI: `http://localhost:8000/docs/`

## Endpoints Principales

- `GET/POST /api/catalogo/categorias/`
- `GET/POST /api/catalogo/experiencias/`
- `GET/POST /api/catalogo/disponibilidades/`

## Estructura del Proyecto

```
ecorutas-backend/
├── core/                 # Configuración principal de Django
├── catalogo/             # App del catálogo de experiencias
│   ├── models.py         # Modelos (Categoria, Experiencia, etc.)
│   ├── views.py          # ViewSets CRUD
│   ├── serializers.py    # Serializers DRF
│   └── urls.py           # Rutas de la API
├── manage.py
└── requirements.txt
```

## Licencia

Proyecto privado - EcoRutas