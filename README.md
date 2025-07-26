# TaskFlow API

TaskFlow es una aplicación de gestión de tareas con IA que sugiere prioridades, estima tiempos y organiza automáticamente tu agenda. Incluye analytics avanzados.

## Tecnologías

- **Python 3.9+**
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **JWT (JSON Web Tokens)** para autenticación

## Estructura del Proyecto

El proyecto sigue una estructura modular para mantener el código organizado y escalable:

```
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── login.py
│   │   │   │   ├── projects.py
│   │   │   │   ├── tasks.py
│   │   │   │   └── dashboard.py
│   │   │   └── api.py
│   │   └── deps.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   ├── crud_user.py
│   │   ├── crud_project.py
│   │   ├── crud_task.py
│   │   └── crud_tag.py
│   ├── db/
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── tag.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── token.py
│   │   └── tag.py
│   └── utils.py
├── .venv/
├── requirements.txt
└── README.md
```

- **`app/api`**: Contiene toda la lógica de la API, incluyendo los endpoints y las dependencias.
- **`app/core`**: Contiene la configuración de la aplicación y la lógica de seguridad.
- **`app/crud`**: Contiene las funciones para interactuar con la base de datos (Crear, Leer, Actualizar, Eliminar).
- **`app/db`**: Contiene la configuración de la base de datos y la gestión de sesiones.
- **`app/models`**: Contiene los modelos de la base de datos (SQLAlchemy).
- **`app/schemas`**: Contiene los esquemas de validación de datos (Pydantic).
- **`app/utils.py`**: Contiene funciones de utilidad, como el envío de correos electrónicos.

## Cómo Ejecutar el Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd taskflow-backend
```

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual (macOS/Linux)
source .venv/bin/activate

# Para desactivar el entorno virtual cuando termines:
# deactivate
```

### 3. Instalar las Dependencias

Asegúrate de que tu entorno virtual esté activado antes de ejecutar este comando.

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

Con el entorno virtual activado, ejecuta la aplicación con Uvicorn.

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`. La opción `--reload` reiniciará el servidor automáticamente cada vez que hagas un cambio en el código.

## Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a la documentación interactiva de la API a través de los siguientes endpoints:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Desde la interfaz de Swagger, podrás ver todos los endpoints disponibles, sus parámetros y esquemas, y probarlos directamente desde el navegador.
