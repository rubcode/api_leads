# 🚀 API de Gestión de Leads

API REST desarrollada con **FastAPI** para registrar y consultar leads.  
El objetivo del proyecto es exponer endpoints simples para almacenar información de leads y poder consultarla posteriormente.

---

# 🧰 Stack Tecnológico

El proyecto fue desarrollado utilizando las siguientes tecnologías:

- **Lenguaje:** Python 3.10+
- **Framework:** FastAPI
- **Validación de datos:** Pydantic
- **Servidor ASGI:** Uvicorn
- **Persistencia:** Archivo JSON
- **Gestión de rutas:** APIRouter de FastAPI

---

# 📂 Estructura del Proyecto


- **routes/** → Contiene los endpoints de la API  
- **schemas/** → Modelos de validación con Pydantic  
- **services/** → Lógica de negocio y persistencia  
- **leads.json** → Almacenamiento de leads  

---

# ⚙️ Instalación y Ejecución en Local

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/leads-api.git
cd leads-api
```
## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows

```bash
venv\Scripts\activate
```
### Mac/Linux

```bash
source venv/bin/activate
```

## 3️⃣ Instalar dependencias

```bash
pip install fastapi uvicorn pydantic email-validator
```

## 4️⃣ Ejecutar la API

```bash
uvicorn main:app --reload
```
### La API estará disponible en:
```bash
http://127.0.0.1:8000
```
# 📡 Endpoints Disponibles

| Método | Endpoint | Descripción             |
|--------|----------|-------------------------|
| GET    | `/`      | Mensaje de bienvenida   |
| POST   | `/leads` | Registrar un nuevo lead |
| GET    | `/leads` | Obtener todos los leads |

# 🧪 Ejemplo de Petición

```bash
curl -X POST "http://127.0.0.1:8000/leads" \
-H "Content-Type: application/json" \
-d '{
  "name": "Juan Pérez",
  "email": "juan@email.com",
  "company": "Empresa Demo",
  "message": "Estoy interesado en sus servicios"
}'
```

# Ejemplo de JSON

```json 
{
  "name": "Juan Pérez",
  "email": "juan@email.com",
  "company": "Empresa Demo",
  "message": "Estoy interesado en sus servicios"
}
```

# Respuesta esperada

```json 
{
  "status": "ok",
  "description": "Lead guardado correctamente",
  "create_at": "2026-03-06 13:00:00",
  "data": {
    "name": "Juan Pérez",
    "email": "juan@email.com",
    "company": "Empresa Demo",
    "message": "Estoy interesado en sus servicios"
  }
}
```

# 🧠 Decisiones de Diseño

## Elección del Stack

Se eligió FastAPI porque es un framework moderno para construir APIs en Python que ofrece alto rendimiento, validación automática de datos con Pydantic, generación automática de documentación con Swagger/OpenAPI, y una sintaxis clara que facilita el desarrollo rápido de servicios backend.

Además, FastAPI permite estructurar el proyecto de forma modular utilizando routers, lo que facilita escalar el proyecto en caso de agregar más endpoints o servicios.

## Manejo de Errores

Los endpoints utilizan bloques try/except para capturar errores inesperados durante la ejecución, como problemas al guardar o leer información de los leads. En caso de error, la API devuelve una respuesta estructurada con un status: error y un mensaje descriptivo para facilitar el diagnóstico del problema.

Adicionalmente, Pydantic valida automáticamente la estructura de los datos de entrada, evitando que se procesen solicitudes con formatos incorrectos.

✅ Autor: Rubén Daniel Rodríguez Rivero
📅 Proyecto: API de Leads con FastAPI