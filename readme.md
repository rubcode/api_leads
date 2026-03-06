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