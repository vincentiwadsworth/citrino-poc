# Desglose de Tareas - Sistema de Recomendación Inmobiliaria

## Fase 1: Preparación de Datos (Commits 1-4)

### 1.1 Estructura de Proyecto
- [ ] Crear directorio principal del proyecto
- [ ] Establecer estructura de carpetas (data, src, tests, docs)
- [ ] Crear archivos requirements.txt y README básico
- [ ] Configurar entorno virtual de Python

### 1.2 Dataset de Propiedades
- [ ] Seleccionar 5 propiedades representativas
- [ ] Crear archivo JSON con estructura de propiedades
- [ ] Incluir características básicas (precio, habitaciones, ubicación)
- [ ] Validar formato y consistencia de datos

### 1.3 Datos de Servicios
- [ ] Obtener datos de guía urbana para áreas seleccionadas
- [ ] Mapear servicios cercanos a cada propiedad (escuelas, hospitales, supermercados)
- [ ] Calcular distancias aproximadas
- [ ] Formatear como JSON estructurado

### 1.4 Datos Demográficos
- [ ] Recopilar datos de censo por zona/vecindario
- [ ] Extraer métricas relevantes (composición familiar, nivel socioeconómico)
- [ ] Asociar datos demográficos a propiedades
- [ ] Crear archivo de datos demográficos JSON

### 1.5 Perfiles de Ejemplo
- [ ] Crear 3 perfiles de prospecto variados:
  - Familia con hijos en edad escolar
  - Pareja joven profesional
  - Adulto mayor
- [ ] Documentar necesidades específicas de cada perfil
- [ ] Validar que perfiles cubran diferentes casos de uso

## Fase 2: Motor de Recomendación (Commits 5-8)

### 2.1 Algoritmo de Matching Básico
- [ ] Implementar función de cálculo de compatibilidad
- [ ] Definir sistema de ponderación (30% presupuesto, 25% familia, 20% servicios, 15% demografía, 10% preferencias)
- [ ] Crear funciones de evaluación por factor
- [ ] Testear con datos de ejemplo

### 2.2 Motor de Recomendación Principal
- [ ] Desarrollar clase principal del motor
- [ ] Implementar método de recomendación
- [ ] Añadir ordenamiento por compatibilidad
- [ ] Crear sistema de límite de resultados (top 5)

### 2.3 Generador de Justificaciones
- [ ] Implementar sistema de generación de explicaciones
- [ ] Crear plantillas para diferentes tipos de匹配
- [ ] Añadir detalles específicos por propiedad recomendada
- [ ] Formato legible para asesores comerciales

### 2.4 Integración de LLM
- [ ] Configurar acceso a OpenRouter/OpenAI
- [ ] Implementar parser de lenguaje natural a perfil estructurado
- [ ] Crear prompts para extracción de información
- [ ] Testear con consultas de ejemplo

## Fase 3: Interfaz de Usuario (Commits 9-12)

### 3.1 CLI Básica
- [ ] Crear script principal con Typer
- [ ] Implementar comando de consulta
- [ ] Añadir opciones de filtrado básico
- [ ] Formato de salida legible

### 3.2 Consulta Conversacional
- [ ] Integrar LLM con CLI
- [ ] Permitir consultas en lenguaje natural
- [ ] Procesar respuestas y mostrar recomendaciones
- [ ] Añadir ejemplos de uso

### 3.3 Utilidades de CLI
- [ ] Comando para ver propiedades disponibles
- [ ] Opción de ajuste de criterios
- [ ] Modo verbose con detalles técnicos
- [ ] Ayuda y documentación integrada

### 3.4 Manejo de Errores
- [ ] Validación de entradas de usuario
- [ ] Manejo de errores de API (LLM)
- [ ] Mensajes de error amigables
- [ ] Logging básico para debugging

## Fase 4: Validación y Demo (Commits 13-16)

### 4.1 Pruebas de Integración
- [ ] Testear flujo completo con los 3 perfiles
- [ ] Validar tiempos de respuesta (< 3 segundos)
- [ ] Verificar calidad de recomendaciones
- [ ] Testear consultas en lenguaje natural

### 4.2 Documentación para Asesores
- [ ] Crear guía de uso para asesores
- [ ] Documentar ejemplos de consultas
- [ ] Explicar cómo interpretar recomendaciones
- [ ] Incluir FAQs y solución de problemas

### 4.3 Demostración Funcional
- [ ] Preparar script de demostración
- [ ] Grabar video del sistema en acción
- [ ] Documentar casos de uso exitosos
- [ ] Recopilar métricas de rendimiento

### 4.4 Feedback y Mejoras
- [ ] Presentar demo a equipo de Citrino
- [ ] Recopilar feedback de asesores
- [ ] Identificar mejoras prioritarias
- [ ] Documentar lecciones aprendidas

## Tareas Adicionales

### Validación Continua
- [ ] Ejecutar pruebas después de cada cambio
- [ ] Verificar consistencia de datos
- [ ] Monitorear rendimiento del algoritmo
- [ ] Actualizar documentación

### Preparación para Escalamiento
- [ ] Documentar arquitectura actual
- [ ] Identificar cuellos de botella
- [ ] Proponer mejoras para futuras versiones
- [ ] Estimar esfuerzo para dataset completo

## Entregables Concretos

1. **Código Funcional**
   - [ ] Motor de recomendación implementado
   - [ ] CLI para consultas en lenguaje natural
   - [ ] Dataset de 5 propiedades con servicios asociados
   - [ ] 3 perfiles de prospecto de ejemplo

2. **Documentación**
   - [ ] Guía de uso para asesores
   - [ ] Documentación técnica del algoritmo
   - [ ] Ejemplos de consultas y respuestas
   - [ ] Registro de decisiones técnicas

3. **Validación**
   - [ ] Demostración funcional grabada
   - [ ] Reporte de rendimiento
   - [ ] Feedback del equipo de Citrino
   - [ ] Recomendaciones para escalamiento

## Estructura de Commits

- **Commits 1-4**: Preparación de datos y estructura
- **Commits 5-8**: Motor de recomendación
- **Commits 9-12**: Interfaz de usuario
- **Commits 13-16**: Validación y demo
- **Commits adicionales**: Mejoras y refinamiento basado en feedback

## Prioridades

1. **Funcionalidad básica primero**: Motor de recomendación funcionando
2. **Validación temprana**: Testear con datos reales lo antes posible
3. **Iteración rápida**: Mejoras incrementales basadas en feedback
4. **Documentación**: Mantener todo documentado para futuros mantenimientos

---

**Fecha**: 20 de septiembre de 2025
**Versión**: 1.0
**Próxima Acción**: Ejecutar `/implement` para comenzar con la primera tarea