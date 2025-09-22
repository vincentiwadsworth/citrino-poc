# Sistema de Recomendación Inmobiliaria para Citrino

## Visión General

Crear un sistema que permita a Citrino analizar datos y recomendar propiedades personalizadas basadas en el perfil detallado de prospectos, integrando datos de inmuebles, características del entorno y demografía.

## Problema a Resolver

Citrino actualmente enfrenta:
- Proceso manual de cruzar necesidades de prospectos con propiedades disponibles
- Dificultad para evaluar múltiples factores simultáneamente (familia, presupuesto, ubicación, servicios cercanos)
- Tiempo perdido en propiedades que no se ajustan a las necesidades reales
- Falta de herramientas para demostrar valor añadido basado en contexto del entorno
- Inconsistencia en las recomendaciones debido al proceso manual

## Objetivo Principal

Desarrollar una herramienta que permita:
- Ingresar perfil detallado del prospecto (composición familiar, presupuesto, necesidades específicas)
- Recomendar automáticamente propiedades que mejor se ajusten a sus necesidades
- Considerar factores de entorno (escuelas, hospitales, supermercados, universidades)
- Proporcionar justificación clara de por qué cada propiedad recomendada es adecuada
- Reducir tiempo del ciclo de ventas y aumentar tasa de conversión

## Alcance del PoC (Proof of Concept)

### Dataset Limitado
- **5 propiedades inmobiliarias** como caso de validación
- Datos de guía urbana georreferenciada asociada
- Información de censo nacional reciente
- 10 perfiles de cliente de ejemplo

### Funcionalidades Mínimas Viables

#### 1. Ingreso de Datos de Prospecto
- **Formulario estructurado** para capturar:
  - Composición familiar (cantidad y edad de miembros)
  - Presupuesto (compra/alquiler)
  - Necesidades educativas (hijos en edad escolar/universitaria)
  - Salud familiar (adultos mayores bajo cuidado)
  - Transporte (cantidad de vehículos)
  - Preferencias de ubicación y estilo de vida

#### 2. Sistema de Recomendación Inteligente
- **Algoritmo de matching** que considere:
  - Ajuste de presupuesto y características de la propiedad
  - Proximidad a servicios requeridos (escuelas, hospitales, supermercados)
  - adecuación demográfica del área
  - Puntuación de compatibilidad (0-100%)

#### 3. Fuentes de Datos Integradas
- **Inmobiliaria Citrino**: Propiedades disponibles, características, precios, detalles del edificio/condominio
- **Guía Urbana**: Ubicación exacta de servicios (escuelas por nivel, hospitales, supermercados, universidades)
- **Censo Nacional**: Datos demográficos por zona, nivel socioeconómico, composición familiar

#### 4. Generación de Recomendaciones
- **Ranking de propiedades** por compatibilidad con perfil
- **Justificación detallada** para cada recomendación
- **Visualización de distancias** a servicios clave
- **Opciones alternativas** si no hay matches perfectos

#### 5. Interfaz para Asesores
- **Consulta conversacional**: "Busca propiedades para familia con 2 hijos en edad escolar, presupuesto $250K"
- **Búsqueda estructurada**: Filtros por presupuesto, ubicación, características
- **Comparación**: Mostrar 2-3 opciones mejores con pros y contras

## Experiencia de Usuario Meta

### Asesores Comerciales deben poder:
1. **Ingresar perfil detallado del prospecto** en 2-3 minutos
2. **Recibir recomendaciones instantáneas** ordenadas por compatibilidad
3. **Entender por qué cada propiedad es recomendada** con justificación clara
4. **Ajustar criterios y ver nuevas recomendaciones** en tiempo real
5. **Mostrar al prospecto opciones personalizadas** durante la reunión

### Ejemplos de Interacción:

**Escenario 1: Asesor ingresa perfil familiar**
```
Asesor: "Necesito propiedades para familia Martinez:
- 4 miembros (padres + 2 hijos de 8 y 12 años)
- Presupuesto: $250-300K
- Necesitan escuela cercana para los niños
- Tienen 1 auto, prefieren zona segura"

Sistema: "Recomendaciones para familia Martinez:

🏆 #1 Casa Norte - $280K (Compatibilidad: 92%)
✓ 3 habitaciones, 2 baños, jardín
✓ Escuela Primaria Norte a 300m (camino seguro)
✓ Supermercado a 500m, Hospital a 1.2km
✓ Zona residencial segura, baja densidad

🥈 #2 Duplex Moderno - $265K (Compatibilidad: 87%)
✓ Espacio familiar amplio
✓ Colegio San José a 600m
✓ Área con familias similares demográficamente

¿Quieres ver detalles de alguna o ajustar criterios?"
```

**Escenario 2: Consulta conversacional**
```
Asesor: "Busca propiedades para pareja joven sin hijos, presupuesto $200K, cerca de universidades"

Sistema: "Encontré 3 opciones ideales para parejas jóvenes:

1. Apartamento Centro - $195K
   • A 400m de Universidad Metropolitana
   • Zona con vida nocturna y restaurantes
   • Ideal para profesionales jóvenes

2. Studio Moderno - $180K
   • A 15 min caminando de campus universitario
   • Gimnasio en edificio, seguridad 24h
   • Popular entre estudiantes y profesores

¿Te interesa alguna en particular?"
```

## Restricciones y Limitaciones

### Técnicas
- Respuestas deben generar en menos de 5 segundos
- Sistema debe utilizar LLM para procesar consultas en lenguaje natural
- No requiere interfaz gráfica compleja inicialmente
- Debe ser mantenible por un solo desarrollador

### De Datos
- Validar con 5 propiedades reales antes de escalar
- Datos de censo pueden ser muestra representativa
- Guía urbana se limita a puntos de interés clave

## Criterios de Éxito

### Funcionales
- [ ] Asesores pueden ingresar perfil completo de prospecto en < 3 minutos
- [ ] Sistema recomienda propiedades con > 85% de precisión de matching
- [ ] Justificaciones de recomendaciones son claras y convincentes
- [ ] Integración de las 3 fuentes de datos funciona correctamente
- [ ] Sistema maneja perfiles familiares diversos (solteros, familias, adultos mayores)

### No Funcionales
- [ ] Tiempo de respuesta < 3 segundos para recomendaciones
- [ ] Interfaz intuitiva que requiere < 30 minutos de entrenamiento
- [ ] Sistema funciona offline durante reuniones con clientes
- [ ] Código y datos pueden ser mantenidos por un solo desarrollador
- [ ] Recomendaciones son consistentes entre diferentes asesores

### de Negocio
- [ ] Reducción del 50% en tiempo de búsqueda de propiedades
- [ ] Aumento del 25% en tasa de conversión de prospectos a clientes
- [ ] Mejora en satisfacción de asesores comerciales
- [ ] Capacidad de escalar a 100+ propiedades sin degradar rendimiento

## Entregables del PoC

1. **Sistema funcional** de recomendación para asesores comerciales
2. **Dataset de prueba** con 5 propiedades + servicios asociados + datos demográficos
3. **3 perfiles de prospecto ejemplo** (familia con hijos, pareja joven, adulto mayor)
4. **Demostración grabada** del sistema haciendo recomendaciones personalizadas
5. **Documentación** para asesores sobre cómo usar el sistema
6. **Evaluación** con equipo de asesores comerciales de utilidad percibida

## Fuera de Alcance (para esta fase)

- Interfaz gráfica web compleja (priorizar CLI/simple web)
- Integración con CRM o sistemas externos en tiempo real
- Procesamiento de documentos escaneados o fotos
- Análisis predictivo de precios o tendencias
- Escalado a dataset completo de Citrino (validar con PoC primero)
- Gestión de inventario o disponibilidad en tiempo real
- Integración con sistemas de pago o financiación

## Próximos Pasos después del PoC

Si el PoC es exitoso:
1. Integrar dataset completo de Citrino
2. Desarrollar interfaz web amigable para asesores
3. Agregar módulo de gestión de prospectos y seguimiento
4. Implementar sistema de aprendizaje para mejorar recomendaciones
5. Integrar con calendario para agendar visitas a propiedades
6. Desarrollar reportes de rendimiento para equipo comercial
7. Considerar versión móvil para uso en terreno

---

**Fecha**: 20 de septiembre de 2025
**Versión**: 2.0
**Prioridad**: Alta
**Stakeholders**: Julio (CEO), Equipo de Asesores Comerciales, Equipo Citrino

**Cambio Mayor**: Modelo actualizado de consulta general a sistema de recomendación específico para asesores comerciales basado en perfil detallado de prospectos.