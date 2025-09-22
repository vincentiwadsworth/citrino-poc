# Plan Técnico de Implementación
# Sistema de Recomendación Inmobiliaria para Asesores Comerciales

## Arquitectura General

### Enfoque de Minimalismo Tecnológico
Basado en la constitución del proyecto, priorizamos simplicidad y mantenibilidad sobre soluciones complejas.

### Componentes Principales

1. **Módulo de Ingesta de Datos**
   - Script Python para procesar datos de las 3 fuentes
   - Formato: JSON/CSV para fácil manipulación
   - Validación de integridad de datos

2. **Motor de Recomendación**
   - Algoritmo de matching basado en reglas y ponderación
   - Cálculo de compatibilidad (0-100%)
   - Generación de justificaciones

3. **Interfaz de Usuario**
   - CLI inicial para validación rápida
   - Posible upgrade a interfaz web simple si se valida el concepto

4. **Almacenamiento**
   - Archivos JSON estructurados (evitar complejidad de DB inicial)
   - Fácil de mantener y respaldar

## Tecnologías Seleccionadas

### Stack Mínimo Viable
- **Python 3.11+**: Lenguaje principal, familiar y con buen ecosistema
- **Pandas**: Para procesamiento de datos estructurados
- **NumPy**: Para cálculos matemáticos y compatibilidad
- **OpenRouter/OpenAI**: Para integración con LLMs y consultas en lenguaje natural
- **LangChain (opcional)**: Para orquestación de LLMs y manejo de prompts
- **FastAPI (opcional)**: Si se necesita interfaz web
- **SQLite**: Para almacenamiento simple si se escala
- **Typer**: Para CLI amigable

### Por qué esta selección?
- **Mantenibilidad**: Un solo desarrollador puede manejar todo el stack
- **Rapidez**: Configuración mínima, enfoque en lógica de negocio
- **Flexibilidad**: Fácil de cambiar tecnologías si es necesario
- **Documentación**: Amplia documentación disponible

## Flujo de Datos

### 1. Ingesta y Procesamiento
```
Fuentes Externas → Scripts Python → Datos Estructurados JSON
```

### 2. Motor de Recomendación
```
Perfil Prospecto + Datos Propiedades → Algoritmo Matching → Recomendaciones Ordenadas
```

### 3. Procesamiento de Lenguaje Natural
```
Consulta en Lenguaje Natural → LLM (OpenRouter/OpenAI) → Perfil Estructurado
```

### 4. Presentación
```
Recomendaciones → Formato Legible → Asesor Comercial
```

## Algoritmo de Matching

### Ponderación de Factores
1. **Presupuesto** (30%): Ajuste exacto o cercano
2. **Composición Familiar** (25%): Habitaciones adecuadas, espacio
3. **Servicios Cercanos** (20%): Distancia a escuelas, hospitales, etc.
4. **Demografía** (15%): Compatibilidad con perfil del área
5. **Preferencias** (10%): Ubicación, estilo de vida

### Cálculo de Compatibilidad
```
Puntuación = Σ(Ponderación_i × Satisfacción_i)
```

Donde Satisfacción_i varía de 0 (no cumple) a 1 (cumple perfectamente)

## Estructura de Datos

### Perfil de Prospecto
```json
{
  "id": "prospecto_001",
  "composicion_familiar": {
    "adultos": 2,
    "ninos": [{"edad": 8}, {"edad": 12}],
    "adultos_mayores": 0
  },
  "presupuesto": {
    "min": 250000,
    "max": 300000,
    "tipo": "compra"
  },
  "necesidades": ["escuela_primaria", "supermercado"],
  "preferencias": {
    "ubicacion": "norte",
    "seguridad": "alta"
  }
}
```

### Propiedad
```json
{
  "id": "propiedad_001",
  "caracteristicas": {
    "precio": 280000,
    "habitaciones": 3,
    "banos": 2,
    "superficie": 120
  },
  "ubicacion": {
    "direccion": "Calle Norte 123",
    "coordenadas": {"lat": -34.5, "lng": -58.5},
    "barrio": "Norte"
  },
  "servicios_cercanos": {
    "escuela_primaria": [{"nombre": "Escuela Norte", "distancia": 300}],
    "supermercado": [{"nombre": "Super Norte", "distancia": 500}]
  }
}
```

## Implementación por Fases

### Fase 1: Datos Iniciales (1 semana)
- [ ] Preparar dataset de 5 propiedades
- [ ] Obtener datos de guía urbana asociada
- [ ] Incorporar datos demográficos de muestra
- [ ] Crear scripts de carga y validación

### Fase 2: Motor de Recomendación (1 semana)
- [ ] Implementar algoritmo de matching básico
- [ ] Desarrollar sistema de ponderación
- [ ] Crear generador de justificaciones
- [ ] Probar con 3 perfiles de ejemplo

### Fase 3: Interfaz de Usuario (3-4 días)
- [ ] Desarrollar CLI para consulta de recomendaciones
- [ ] Implementar formato de salida legible
- [ ] Agregar opciones de filtrado y ajuste
- [ ] Probar usabilidad con asesores

### Fase 4: Validación y Demo (2-3 días)
- [ ] Realizar demostración con equipo de asesores
- [ ] Recopilar feedback y ajustar algoritmo
- [ ] Documentar lecciones aprendidas
- [ ] Preparar recomendaciones para escalamiento

## Estrategia de Desarrollo

### Principios Guía
1. **Validación Temprana**: Cada fase se valida con usuarios reales
2. **Simplicidad**: No añadir complejidad hasta que sea necesario
3. **Documentación**: Código autodocumentado y comentarios claros
4. **Pruebas**: Validar cada componente con datos reales

### Manejo de Riesgos
- **Riesgo Técnico**: Mantener código simple y modular para facilitar cambios
- **Riesgo de Datos**: Validar calidad de datos desde el inicio
- **Riesgo de Usabilidad**: Involucrar a asesores desde fases tempranas

## Métricas de Éxito Técnico

### Rendimiento
- Tiempo de respuesta < 3 segundos para recomendaciones
- Uso de memoria < 100MB para dataset de PoC
- Tiempo de procesamiento de datos < 30 segundos

### Calidad
- Cobertura de tests > 80%
- Documentación completa de API y algoritmos
- Código遵循 PEP 8 y buenas prácticas

### Mantenibilidad
- Complejidad ciclomática baja (< 10 por función)
- Acoplamiento mínimo entre módulos
- Fácil de extender con nuevas fuentes de datos

## Próximos Pasos

1. **Inmediato**: Comenzar con Fase 1 (preparación de datos)
2. **Paralelo**: Diseñar estructura detallada de archivos y módulos
3. **Validación**: Coordinar con equipo de Citrino para pruebas tempranas

---

**Fecha**: 20 de septiembre de 2025
**Versión**: 1.0
**Próxima Acción**: Ejecutar `/tasks` para desglosar este plan en tareas concretas