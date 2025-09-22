# Docker Guide - Citrino PoC

Esta guía explica cómo usar Docker para desplegar y ejecutar el sistema de recomendación inmobiliaria en cualquier equipo.

## 🐳 Prerrequisitos

- Docker instalado en el sistema
- Docker Compose (opcional, pero recomendado)
- Credenciales de API para LLM (OpenRouter/OpenAI)

## LANZAR: Construcción y Ejecución

### Opción 1: Usar Docker Compose (Recomendado)

1. **Configurar variables de entorno**:
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env

   # Editar el archivo .env con tus API keys
   nano .env
   ```

2. **Construir y ejecutar el contenedor**:
   ```bash
   docker-compose up --build
   ```

3. **Ejecutar comandos específicos**:
   ```bash
   # Listar propiedades
   docker-compose run --rm citrino-poc python -m src.cli listar-propiedades

   # Recomendar con perfil
   docker-compose run --rm citrino-poc python -m src.cli recomendar --perfil "familia con 2 hijos"

   # Ver ayuda
   docker-compose run --rm citrino-poc python -m src.cli ayuda
   ```

### Opción 2: Usar Docker directamente

1. **Construir la imagen**:
   ```bash
   docker build -t citrino-poc .
   ```

2. **Ejecutar el contenedor**:
   ```bash
   docker run -it --rm \
     -v $(pwd)/data:/app/data \
     -v $(pwd)/scripts:/app/scripts \
     -e OPENROUTER_API_KEY=tu_api_key \
     -e OPENAI_API_KEY=tu_api_key \
     citrino-poc python -m src.cli ayuda
   ```

3. **Ejecutar comandos específicos**:
   ```bash
   docker run -it --rm \
     -v $(pwd)/data:/app/data \
     -e OPENROUTER_API_KEY=tu_api_key \
     citrino-poc python -m src.cli listar-propiedades
   ```

## 📁 Volúmenes y Persistencia

### Data Persistence
Los siguientes directorios se montan como volúmenes para persistencia de datos:
- `./data:/app/data` - Dataset de propiedades y perfiles
- `./scripts:/app/scripts` - Scripts de procesamiento
- `./docs:/app/docs` - Documentación

### Environment Variables
- `OPENROUTER_API_KEY`: API key para OpenRouter
- `OPENAI_API_KEY`: API key para OpenAI
- `PYTHONPATH`: Path de Python dentro del contenedor

## CONFIG: Desarrollo con Docker

### Modo Desarrollo
Para desarrollo, puedes usar Docker Compose con hot-reload:

```bash
# Construir imagen de desarrollo
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### Testing en Docker
Ejecutar pruebas dentro del contenedor:

```bash
docker-compose run --rm citrino-poc pytest
```

### Linting en Docker
Verificar calidad del código:

```bash
docker-compose run --rm citrino-poc flake8 src/
```

## 🏗️ Arquitectura del Contenedor

### Imagen Base
- **Python 3.11-slim**: Imagen ligera y optimizada
- **Seguridad**: Usuario no-root (appuser)
- **Optimización**: Multi-stage build no necesario para este PoC

### Dependencias
- **System**: gcc, g++ para compilación de paquetes
- **Python**: Todas las dependencias del requirements.txt
- **Application**: Código fuente, datos y scripts

### Seguridad
- Usuario no-root (appuser)
- Variables de entorno sensibles
- Volúmenes controlados
- .dockerignore para archivos innecesarios

## LANZAR: Despliegue en Producción

### Variables de Entorno Requeridas
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_KEY=your_openai_api_key
PYTHONPATH=/app
```

### Comandos de Producción
```bash
# Construir imagen optimizada
docker build -t citrino-poc:latest .

# Ejecutar en producción
docker run -d \
  --name citrino-poc-prod \
  -v /path/to/data:/app/data \
  -e OPENROUTER_API_KEY=prod_api_key \
  -e OPENAI_API_KEY=prod_api_key \
  citrino-poc:latest
```

### Monitoreo
```bash
# Ver logs
docker logs citrino-poc

# Ver estado del contenedor
docker ps

# Acceder al contenedor (debugging)
docker exec -it citrino-poc bash
```

## CONFIG: Solución de Problemas

### Problemas Comunes

1. **Permisos de archivos**:
   ```bash
   # Asegurar permisos correctos
   sudo chown -R $USER:$USER data/
   ```

2. **Variables de entorno no cargadas**:
   ```bash
   # Verificar variables en contenedor
   docker exec citrino-poc env
   ```

3. **Problemas de red**:
   ```bash
   # Verificar red Docker
   docker network ls
   docker network inspect citrino-poc_citrino-network
   ```

4. **Construcción fallida**:
   ```bash
   # Limpiar caché de Docker
   docker system prune -a
   docker builder prune -a
   ```

### Logs y Debugging
```bash
# Ver logs en tiempo real
docker-compose logs -f citrino-poc

# Acceder al contenedor para debugging
docker exec -it citrino-poc bash

# Verificar recursos del contenedor
docker stats citrino-poc
```

## 📋 Checklist de Despliegue

- [ ] Docker instalado y funcionando
- [] Variables de entorno configuradas
- [ ] Archivos de datos disponibles
- [ ] Permisos de archivos correctos
- [ ] Red Docker funcionando
- [ ] API keys válidas
- [ ] Contenedor construido exitosamente
- [ ] Comandos básicos funcionando
- [ ] Logs mostrando información esperada

---

**Última actualización**: 20 de septiembre de 2025
**Versión**: 1.0
**Estado**: Configuración Docker completa para despliegue universal