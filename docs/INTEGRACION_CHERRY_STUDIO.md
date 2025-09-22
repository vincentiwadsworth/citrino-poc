# Integración Cherry Studio + Citrino API

## Visión General

Implementación de un sistema que permite **"chatear con la información"** inmobiliaria usando Cherry Studio como interfaz conversacional.

## Arquitectura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Cherry Studio │    │   Chat Citrino   │    │   Citrino API   │    │   Base de       │
│   (Interfaz)    │───▶│   Bridge         │───▶│   (Motor)       │───▶│   Datos         │
│                 │    │   (LLM + Logic)  │    │                 │    │   (76,853 props)│
└─────────────────┘    └──────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         └───────────────────────┼───────────────────────┼───────────────────────┘
                                │                       │
                                ▼                       ▼
                        ┌──────────────────┐    ┌─────────────────┐
                        │   OpenAI LLM    │    │   Municipal     │
                        │   (Análisis)    │    │   Data          │
                        └──────────────────┘    └─────────────────┘
```

## Flujo de Conversación

1. **Usuario pregunta en Cherry Studio**: *"Busco departamentos en Equipetrol para familia joven"*

2. **LLM analiza y extrae parámetros**:
   ```json
   {
     "presupuesto_min": 150000,
     "presupuesto_max": 250000,
     "zona": "Equipetrol",
     "tipo_propiedad": "departamento",
     "adultos": 2,
     "ninos": [1],
     "consulta_tipo": "recomendacion"
   }
   ```

3. **API Citrino procesa**: Busca en 76,853 propiedades + 8,623 datos municipales

4. **LLM sintetiza respuesta conversacional**:
   ```
   "Hola! Entiendo que buscas un departamento en Equipetrol para tu familia.
   He encontrado 3 opciones excelentes dentro de tu presupuesto..."
   ```

## Configuración Cherry Studio

### Opción 1: Usar como API Externa

En Cherry Studio, configurar un nuevo asistente con:

```
Nombre: Asesor Citrino
Base URL: http://localhost:8000  # Nuestro bridge
Model: citrino-chat
API Key: tu-key
```

### Opción 2: Integración Directa

1. Cherry Studio ya está instalado en Citrino
2. Configurar para consumir nuestro bridge local
3. Los usuarios chatean naturalmente como lo hacen normalmente

## Implementación Técnica

### Componentes Principales:

1. **chat_citrino_bridge.py**: Puente principal
   - Recibe consultas de Cherry Studio
   - Procesa con LLM para extraer parámetros
   - Consulta API Citrino
   - Sintetiza respuestas

2. **API Citrino (existente)**: Motor de recomendación
   - Base de datos de propiedades
   - Inteligencia de mercado
   - Datos municipales

3. **OpenAI LLM**: Cerebro de procesamiento
   - Análisis de lenguaje natural
   - Extracción de parámetros
   - Síntesis de respuestas

## Ejemplos de Uso

### Consulta Simple:
```
Usuario: "Busco casas en Las Palmas con presupuesto de 300k"
Asesor: "He encontrado 5 casas excelentes en Las Palmas dentro de tu presupuesto..."
```

### Consulta Compleja:
```
Usuario: "Necesito un departamento para inversión en Equipetrol,
         que tenga buena plusvalía y sea atractivo para alquiler"
Asesor: "Para tu estrategia de inversión en Equipetrol, he identificado 3
         propiedades con alto potencial de plusvalía..."
```

### Consulta de Mercado:
```
Usuario: "¿Cómo está el mercado de propiedades en Zona Norte?"
Asesor: "El mercado en Zona Norte muestra una tendencia alcista con un
         precio promedio de $185,000 y alta demanda..."
```

## Ventajas para Citrino

### ✅ Para el Equipo de Citrino:
- **Interfaz familiar**: Usan Cherry Studio habitualmente
- **Lenguaje natural**: No necesitan aprender consultas técnicas
- **Resultados en tiempo real**: Acceso a 76,853 propiedades instantáneamente
- **Respuestas profesionales**: Síntesis inteligente de datos

### ✅ Para los Clientes:
- **Atención personalizada**: Respuestas adaptadas a necesidades específicas
- **Información completa**: Acceso a toda la base de datos de Citrino
- **Recomendaciones inteligentes**: Basadas en inteligencia de mercado
- **Experiencia conversacional**: Natural e intuitiva

## Próximos Pasos

1. **Configurar variables de entorno**: API keys y endpoints
2. **Probar bridge local**: `python chat_citrino_bridge.py`
3. **Integrar con Cherry Studio**: Configurar como API externa
4. **Pruebas con equipo Citrino**: Validar experiencia de usuario
5. **Mejoras continuas**: Ajustar prompts y respuestas

## Impacto Estratégico

Esta implementación transforma la base de datos de Citrino en un **asesor inmobiliario conversacional** que:

- **Democratiza el acceso** a la información inmobiliaria
- **Aumenta la productividad** del equipo comercial
- **Mejora la experiencia** de clientes y prospectos
- **Posiciona a Citrino** como líder en tecnología inmobiliaria

---
**Estado**: En implementación
**Próximo hito**: Pruebas con equipo Citrino
**Impacto**: Transformación digital del servicio inmobiliario