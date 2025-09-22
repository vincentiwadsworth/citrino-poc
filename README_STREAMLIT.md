# Demo Citrino API - Streamlit

## Configuración

### 1. Iniciar Servidor API
```bash
cd api
python server.py
```
Verificar que está corriendo en `http://localhost:5000`

### 2. Instalar Streamlit
```bash
pip install streamlit requests
```

### 3. Ejecutar Demo
```bash
streamlit run demo_simple.py
```

Se abrirá automáticamente en tu navegador: `http://localhost:8501`

## Características de la Demo

### 🔍 Búsqueda Interactiva
- Filtros por presupuesto, zona, tipo de propiedad
- Resultados en tiempo real de 76,853 propiedades
- Interface intuitiva con sliders y selectores

### 🎯 Sistema de Recomendación
- Demo pre-configurada: Familia joven en Equipetrol
- Muestra compatibilidad y justificaciones
- Resultados con scoring personalizado

### 📊 Visualización Profesional
- Diseño limpio y corporativo
- Expanders para detalles de propiedades
- Mensajes de error amigables
- Indicadores de carga

## Especificaciones Técnicas

### Base de Datos
- 76,853 propiedades comerciales validadas
- 323 proyectos con inteligencia de mercado
- 8,623 puntos de datos municipales

### API Endpoints
- `GET /api/health` - Verificación de estado
- `POST /api/buscar` - Búsqueda por filtros
- `POST /api/recomendar` - Recomendaciones personalizadas
- `GET /api/estadisticas` - Estadísticas de mercado
- `GET /api/zonas` - Lista de zonas disponibles

### Rendimiento
- Tiempo de respuesta < 2 segundos
- 100% tasa de éxito en pruebas
- Soporte para consultas concurrentes

## Troubleshooting

### Verificar estado del servidor API:
```bash
curl http://localhost:5000/api/health
```

### Instalar dependencias:
```bash
python -m pip install streamlit requests
```

### Errores comunes:
- **Connection refused**: Asegúrate que el servidor API esté corriendo en puerto 5000
- **File not found**: Verifica que los archivos de datos existan en `data/bd_final/`
- **Module errors**: Instala las dependencias faltantes

## Acceso Directo

La demo permite:
- **Búsqueda filtrada**: Por presupuesto, zona, tipo de propiedad
- **Recomendaciones automáticas**: Basadas en perfil familiar
- **Exploración de datos**: Ver detalles de cada propiedad
- **Pruebas en tiempo real**: Sin necesidad de recargar

## Arquitectura

```
Streamlit UI → API Citrino → Base de Datos
     ↓              ↓            ↓
Interfaz     Motor de      76,853
Interactiva  Recomendación  Propiedades
```

## Personalización

Puedes modificar:
- **Filtros**: Agregar nuevos parámetros de búsqueda
- **Diseño**: Cambiar colores y layout
- **Perfiles**: Configurar diferentes tipos de recomendaciones
- **Datos**: Conectar a otras fuentes de información