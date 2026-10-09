# EcoRutas Backend

Backend API para la aplicación EcoRutas, construida con Django y Django REST Framework.

## Tecnologías

- Python 3.12 (Recomendado)
- Django 6.1.2
- Django REST Framework 3.18.3
- drf-yasg (Documentación Swagger)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/saithfortxd1/ecorutas-backend.git
cd ecorutas-backend

# Crear entorno virtual
py -3.12 -m venv venv   # O bien: python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate

# En Windows (PowerShell):
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  # Ejecutar si Windows bloquea scripts
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Ejecutar server
python manage.py runserver

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
