# Citrino POC Constitution

## Core Principles

### I. Valor Sobre Tecnología (NON-NEGOTIABLE)
El objetivo principal es resolver el problema de Julio (CEO) para que pueda "chatear con los datos". Las tecnologías son herramientas, no el fin. Cada decisión técnica debe justificarse por cómo contribuye al valor de negocio inmediato.

### II. Enfoque en el Usuario Final
Desarrollar para Julio y el equipo de Citrino, no para desarrolladores. La interfaz debe ser lenguaje natural, no técnica. Priorizar usabilidad sobre complejidad técnica.

### III. Datos Inmobiliarios + Guía Urbana + Censo
El sistema debe integrar tres fuentes de datos específicas:
1. Información inmobiliaria de Citrino (disponibilidad, características, precio)
2. Guía urbana georreferenciada de la Alcaldía
3. Datos de censo nacional reciente

### IV. Progresos Tangibles Rápidos
Entregar valor incremental cada semana. Mejor una solución funcional simple que una arquitectura perfecta que nunca se termina. Validar con usuarios reales frecuentemente.

### V. Simplicidad y Mantenibilidad
Elegir tecnologías familiares y bien documentadas. Priorizar soluciones que un solo desarrollador pueda mantener y extender. Documentar decisiones para evitar retrabajo.

### VI. TDAH-Amigable
Proceso de desarrollo que acomode TDAH: tareas claras y concretas, tiempo limitado de enfoque, documentación visual, reducción de distracciones técnicas.

## Restricciones del Proyecto

### Alcance
- PoC (Proof of Concept) con dataset limitado: 5 inmuebles iniciales
- Validar arquitectura antes de escalar a dataset completo
- Demostración funcional vs sistema productivo completo

### Plazo
- Enfoque en validación rápida: semanas no meses
- Iteraciones cortas con feedback constante
- Priorizar velocidad de aprendizaje sobre perfección

### Tecnología
- Flexibilidad para cambiar tecnologías basadas en resultados
- No atarse a soluciones "shiny" sin validación práctica
- Preparado para pivotar según aprendizaje

## Flujo de Desarrollo

### Spec-Driven Development
1. **Constitution**: Principios que guían todas las decisiones
2. **Specify**: Definir QUÉ se necesita, no CÓMO implementarlo
3. **Plan**: Decidir tecnología mínima viable
4. **Tasks**: Tareas concretas y realizables
5. **Implement**: Ejecutar sin sobre-ingeniería

### Calidad
- Tests automatizados para funcionalidad crítica
- Validación manual con usuarios (Julio/equipo)
- Documentación clara y concisa
- Código que el futuro yo pueda entender

## Governance

### Autoridad
Esta constitución supersedes todas las prácticas técnicas. Cualquier decisión que viole estos principios requiere justificación explícita.

### Proceso de Enmienda
Los cambios a esta constitución deben:
1. Documentar el problema con el enfoque actual
2. Explicar cómo el cambio mejora el valor para Julio
3. Aprobación por el desarrollador (uno mismo)

### Cumplimiento
Todas las características y decisiones técnicas deben verificar el cumplimiento con estos principios. La complejidad debe justificarse por valor de negocio demostrable.

**Versión**: 1.0.0 | **Ratificado**: 2025-09-20 | **Last Amended**: 2025-09-20