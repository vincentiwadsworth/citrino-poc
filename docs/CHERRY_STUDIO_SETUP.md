# Configuración de Cherry Studio para Citrino

## Requisitos Previos

1. **Cherry Studio** instalado (versión 1.0.3 o superior)
2. **Python 3.11+** con el entorno virtual de Citrino activado
3. **API Key** de OpenRouter o OpenAI (configurada en el proyecto)

## Pasos de Configuración

### 1. Instalar Cherry Studio

```bash
# Usando npm (recomendado)
npm install -g @cherrystudio/cli

# O usando pip
pip install cherrystudio
```

### 2. Configurar Variables de Entorno

Cherry Studio necesita acceso a las mismas variables de entorno que el proyecto Citrino:

```bash
# En tu terminal (Windows PowerShell)
$env:OPENROUTER_API_KEY = "tu-api-key-aqui"
$env:OPENAI_API_KEY = "tu-openai-key-aqui"
```

### 3. Configurar Proyecto en Cherry Studio

```bash
# Inicializar Cherry Studio en el directorio del proyecto
cd "C:\Users\nicol\OneDrive\Documentos\trabajo\citrino\citrino-poc"
cherry studio init

# Configurar el proyecto
cherry studio config set name "Citrino PoC"
cherry studio config set type "python"
cherry studio config set entrypoint "python -m src.cli"
```

### 4. Crear Archivo de Configuración

Crea un archivo `cherry.yml` en la raíz del proyecto:

```yaml
name: "Citrino PoC"
type: "python"
version: "1.0.0"
description: "Sistema de recomendación inmobiliaria para Citrino"

# Variables de entorno necesarias
env:
  - OPENROUTER_API_KEY
  - OPENAI_API_KEY

# Comandos disponibles
commands:
  test: "python -m pytest"
  cli: "python -m src.cli"
  validate: "python -m scripts.validar_dataset_mejorado"

# Archivos a monitorear
watch:
  - "src/**/*.py"
  - "data/*.json"
  - "tests/**/*.py"
```

### 5. Probar la Configuración

```bash
# Iniciar Cherry Studio
cherry studio start

# Probar el CLI de Citrino
cherry studio run cli recomendar --perfil "pareja joven, presupuesto 200K, cerca de universidades"

# Probar con un perfil específico
cherry studio run cli recomendar --perfil data/perfiles_ejemplo.json --limite 3 --formato tabla
```

## Ejemplos de Uso para Reunión

### 1. Recomendación para Familia

```bash
cherry studio run cli recomendar \
  --perfil "familia con 2 hijos, presupuesto 250-300K, necesita escuela cercana" \
  --limite 3 \
  --formato detallado
```

### 2. Recomendación para Pareja Joven

```bash
cherry studio run cli recomendar \
  --perfil "pareja joven profesional, presupuesto 180-250K, cerca de universidades" \
  --limite 5 \
  --formato json
```

### 3. Listar Propiedades Disponibles

```bash
cherry studio run cli listar-propiedades
```

### 4. Validación del Sistema

```bash
cherry studio run validate
```

## Solución de Problemas

### Problemas Comunes

1. **ModuleNotFoundError**: Asegúrate de estar en el directorio correcto y con el entorno virtual activado

2. **API Key no encontrada**: Verifica que las variables de entorno estén configuradas correctamente

3. **Unicode errors**: El proyecto ya incluye solución para caracteres Unicode en Windows

### Logs y Depuración

```bash
# Ver logs de Cherry Studio
cherry studio logs

# Modo verbose
cherry studio run cli --verbose recomendar --perfil "test"
```

## Integración con Workflow

### Durante la Reunión

1. **Demostración Rápida**:
   ```bash
   cherry studio run cli recomendar --perfil "familia tipo, presupuesto 250K"
   ```

2. **Mostrar Dataset Completo**:
   ```bash
   cherry studio run cli listar-propiedades
   ```

3. **Probar Diferentes Perfiles**:
   ```bash
   cherry studio run cli recomendar --perfil "adulto mayor, presupuesto 150K"
   ```

### Post-Reunión

1. **Guardar Configuración**:
   ```bash
   cherry studio config save citrino-config.json
   ```

2. **Exportar Resultados**:
   ```bash
   cherry studio run cli recomendar --perfil perfil.json --formato json > resultados.json
   ```

## Notas para la Presentación

- El sistema está optimizado para 20 propiedades reales
- Utiliza campos determinantes: superficie, habitaciones, baños, garaje
- Incluye zonas premium de Santa Cruz: Equipetrol, Las Palmas, Urubó, Zona Norte
- El motor de recomendación evalúa 5 factores con diferentes ponderaciones
- Tiempo de respuesta promedio: 0.21ms por recomendación

## Contacto

Si encuentras problemas durante la configuración:
1. Revisa los logs con `cherry studio logs`
2. Verifica la configuración en `cherry.yml`
3. Asegúrate de tener todas las dependencias instaladas