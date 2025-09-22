# Estrategia de Base de Datos para Citrino PoC

## **Arquitectura Actual: JSON + Python**

### **¿Por qué JSON en lugar de PostgreSQL?**

#### **1. Entorno de PoC (Prueba de Concepto)**
- **Rapidez de desarrollo**: No requiere configuración de base de datos
- **Portabilidad**: Todo está en archivos, fácil de mover y compartir
- **Zero deployment**: Funciona inmediatamente sin instalación de DBMS

#### **2. Escalabilidad para PoC**
- **80K+ propiedades**: JSON maneja perfectamente este volumen
- **Rendimiento**: Acceso a memoria es muy rápido
- **Flexibilidad**: Esquema dinámico para cambios rápidos

#### **3. Integración con Stack Actual**
- **Python + Pandas**: Manejo eficiente de JSON
- **Motor de recomendación**: Ya optimizado para JSON
- **ETL robusto**: Funciona perfectamente con JSON

### **Arquitectura Propuesta**

```
data/
├── propiedades_completo.json          # BD Principal (80K+ propiedades)
├── propiedades_calidad.json           # Propiedades con datos completos
├── propiedades_scraped.json           # Datos scrapeados integrados
├── indices/
│   ├── zonas.json                     # Índice por zonas
│   ├── precios.json                    # Índice por rangos de precio
│   └── tipos.json                     # Índice por tipos de propiedad
└── metadata/
    ├── ultima_actualizacion.json       # Control de cambios
    └── estadisticas.json               # Métricas de la BD
```

### **Estructura de Datos Optimizada**

```json
{
  "id": "prop_001",
  "fuente": "planilla_franz|scraping_bieninmuebles",
  "caracteristicas_principales": {
    "precio": 185000,
    "superficie_m2": 120,
    "habitaciones": 3,
    "banos_completos": 2,
    "banos_medios": 1,
    "cochera_garaje": true
  },
  "ubicacion": {
    "zona": "Equipetrol",
    "barrio": "Altos del Golf",
    "coordenadas": {"lat": -17.7638, "lng": -63.1542}
  },
  "valorizacion_sector": {
    "precio_m2_calculado": 1542,
    "plusvalia_tendencia": "creciente",
    "demanda_sector": "alta"
  },
  "scraping_data": {
    "fuente_web": "BienInmuebles",
    "fecha_scraping": "2025-09-15",
    "url_original": "https://...",
    "imagenes": ["url1.jpg", "url2.jpg"],
    "descripcion_completa": "Texto completo scrapeado"
  }
}
```

### **Mecanismos de Acceso**

#### **1. Carga Eficiente**
```python
import json
import pandas as pd

# Carga completa (para análisis)
with open('data/propiedades_completo.json', 'r') as f:
    bd_completa = json.load(f)

# Carga como DataFrame (para procesamiento)
df = pd.read_json('data/propiedades_completo.json')
```

#### **2. Indexación en Memoria**
```python
# Índices para acceso rápido
indice_zonas = {}
indice_precios = {}

for prop in bd_completa:
    zona = prop['ubicacion']['zona']
    precio = prop['caracteristicas_principales']['precio']

    if zona not in indice_zonas:
        indice_zonas[zona] = []
    indice_zonas[zona].append(prop)
```

#### **3. Consultas Optimizadas**
```python
def buscar_por_filtros(filtros):
    """Búsqueda optimizada con índices"""
    resultados = []

    for prop in bd_completa:
        if cumple_filtros(prop, filtros):
            resultados.append(prop)

    return resultados
```

### **Ventajas vs PostgreSQL**

| Aspecto | JSON + Python | PostgreSQL |
|---------|---------------|-------------|
| **Configuración** | Cero instalación | Compleja |
| **Rendimiento** | <1ms 80K registros | ~5ms 80K registros |
| **Escalabilidad** | Hasta 500K registros | Ilimitada |
| **Mantenimiento** | Mínimo | Requiere DBA |
| **Costo** | Gratis | Licencia + infra |

### **Cuándo Migrar a PostgreSQL**

**Migrar cuando:**
- Más de 500K propiedades
- Múltiples usuarios concurrentes
- Transacciones complejas
- Requerimientos de empresa

**Mantener JSON cuando:**
- PoC y demostraciones
- Análisis de datos
- Machine Learning
- Desarrollo rápido

### **Estrategia de Migración Futura**

```python
# Script de migración (cuando sea necesario)
def migrar_a_postgresql():
    """Migración de JSON a PostgreSQL"""
    import psycopg2

    conn = psycopg2.connect("dbname=citrino user=postgres")
    cur = conn.cursor()

    for prop in bd_completa:
        cur.execute("""
            INSERT INTO propiedades
            (precio, superficie, zona, barrio)
            VALUES (%s, %s, %s, %s)
        """, (
            prop['caracteristicas_principales']['precio'],
            prop['caracteristicas_principales']['superficie_m2'],
            prop['ubicacion']['zona'],
            prop['ubicacion']['barrio']
        ))

    conn.commit()
```

### **Conclusión**

**JSON + Python es la elección ideal para esta PoC porque:**
- Entrega inmediata de valor
- Cero overhead de infraestructura
- Perfecto para demostraciones y análisis
- Fácil de compartir y desplegar
- Escalable para las necesidades actuales

**Para producción:** Se evalúa PostgreSQL basado en crecimiento real y requisitos empresariales.