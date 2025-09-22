<smtcmp_block filename="Changelog - Evolución Proyecto Citrino.md" language="markdown">
# Changelog - Evolución del Proyecto Citrino

## Propuesta de Valor Original

**Problema Identificado:** Fragmentación de datos en múltiples planillas que impedían consultas cruzadas y análisis relacional complejo.

**Valor Prometido:** Sistema de consulta en lenguaje natural capaz de procesar relaciones complejas entre inmuebles, clientes y contexto urbano.

---

## Versión 1.0 - Propuesta Inicial
**Fecha:** Inicio del proyecto  
**Enfoque:** Base de datos relacional tradicional

**Arquitectura Original:**
- **Tecnología:** PostgreSQL (modelo relacional)
- **Enfoque:** Migración directa de Excel a tablas relacionales
- **Timeline:** 8 semanas (Análisis → Implementación → Optimización)

**Entregables Planificados:**
- Base de datos centralizada, poblada, optimizada y segura
- Manual técnico completo en formato Markdown
- Scripts SQL y Python utilizados en el proyecto

---

## Versión 2.0 - Pivote a Grafos
**Fecha:** 15 de septiembre, 2025  
**Cambio Mayor:** Migración de modelo relacional a base de datos de grafos

### Justificación del Cambio

**Modelo Relacional (ej. PostgreSQL):**
- Requiere múltiples `JOINs` para consultas de 3 o más niveles de relación
- El rendimiento se degrada exponencialmente con la complejidad de la consulta

**Modelo de Grafo (Neo4j):**
- Las relaciones son entidades de primer nivel
- Las consultas atraviesan conexiones directas, manteniendo rendimiento alto y predecible

**Conclusión:** Para el caso de uso de Citrino, centrado en relaciones, el modelo de grafo reduce la latencia de las consultas complejas en órdenes de magnitud.

### Nueva Arquitectura

**Componentes:**
1. **Ingesta y ETL:** Scripts de Python para extraer, transformar y cargar datos
2. **Base de Datos de Grafos (Neo4j):** Almacenamiento centralizado
3. **API de Consulta (Cherry Studio):** Endpoint para peticiones en lenguaje natural
4. **Orquestador de LLMs (OpenRouter):** Traducción de lenguaje natural a consultas Cypher

---

## Versión 2.1 - Enfoque PoC
**Fecha:** 15 de septiembre, 2025  
**Refinamiento:** Implementación mediante Prueba de Concepto

### Cambio de Estrategia

**Objetivo:** Validar la viabilidad de la arquitectura propuesta y el flujo de datos completo a escala reducida.

**Alcance Definido:**
- **Dataset:** 5 inmuebles, datos del censo asociados, 10 perfiles de cliente
- **Funcionalidad:** Capacidad de ingestar datos y ejecutar 3 tipos de consultas predefinidas
- **Entregable:** Endpoint funcional y demostración grabada del proceso

**De desarrollo completo a validación dirigida:**
- **Alcance reducido:** 5 inmuebles vs. dataset completo
- **Objetivo:** Validar arquitectura antes de escalar
- **Entregable:** Demostración funcional vs. sistema productivo

### Dataset de Validación
- **Inmuebles Analizados:** 5 propiedades seleccionadas
- **Datos de Servicios:** Información complementaria de la guía urbana
- **Puntos de Interés (Guía Urbana):** Escuelas, Supermercados, Hospitales

---

## Versión 2.2 - Implementación Práctica
**Fecha:** 15 de septiembre, 2025  
**Estado:** Primera validación técnica completada

### Hito Alcanzado
Se ha completado con éxito la primera fase de la ingesta de datos (ETL), validando el flujo desde una fuente de datos tabular (Excel) hacia la base de datos de grafos (Neo4j).

### Progreso Técnico
1. **Desarrollo del Script de Ingesta:** Script Python (`cargar_datos.py`) con pandas y neo4j
2. **Extracción y Transformación:** Lectura exitosa de `GUIA URBANA.xlsx`
3. **Carga y Modelado:** Datos procesados cargados en base de datos `guia-urbana-db`
4. **Verificación y Validación:** Comprobaciones de integridad de datos

### Validación del Modelo
**Ejemplo de consulta validada:**
- **Lenguaje Natural:** "Muéstrame los micromercados que están en la Zona Oeste"
- **Cypher ejecutado:**
  ```cypher
  MATCH (p:PuntoDeInteres {nombre: 'MICROMERCADO'})-[:UBICADO_EN]->(b:Barrio)-[:DENTRO_DE]->(uv:UV)-[:EN_ZONA]->(z:Zona {nombre: 'Oeste'})
  RETURN p.nombre, p.direccion, b.nombre AS barrio
  ```

---

## Evolución de Entregables

### Original (v1.0)
- Base de datos centralizada, poblada, optimizada y segura
- Manual técnico completo
- Scripts SQL y Python

### Actual (v2.2)
- Endpoint funcional para consultas
- Demostración grabada del proceso
- 3 consultas predefinidas ejecutándose correctamente

---

## Análisis de Cambios Estratégicos

### Cambios Tecnológicos Mayores
1. **Arquitectura de Datos:** Relacional → Grafos
2. **Base de Datos:** PostgreSQL → Neo4j
3. **Lenguaje de Consulta:** SQL → Cypher
4. **Enfoque de Desarrollo:** Waterfall → PoC iterativa

### Cambios en el Alcance
1. **Timeline:** 8 semanas → Validación inmediata
2. **Dataset:** Completo → Muestra de 5 inmuebles
3. **Entregable:** Sistema productivo → Demostración funcional

### Invariantes (Valor Mantenido)
- **Objetivo:** Consultas en lenguaje natural
- **Problema:** Fragmentación de datos
- **Beneficio:** Análisis relacional complejo
- **Usuario:** Equipos de Citrino

---

## Riesgos y Oportunidades del Pivote

### Riesgos Mitigados
- **Complejidad de JOINs:** Eliminada con modelo de grafos
- **Escalabilidad de consultas:** Mejorada significativamente
- **Tiempo de desarrollo:** Reducido con enfoque PoC

### Nuevos Riesgos Introducidos
- **Curva de aprendizaje:** Neo4j/Cypher vs. SQL familiar
- **Ecosistema:** Menos maduro que PostgreSQL
- **Integración:** APIs específicas para grafos

### Oportunidades Creadas
- **Diferenciación:** Arquitectura avanzada para inmobiliaria
- **Escalabilidad:** Mejor preparación para crecimiento
- **IA Integration:** Modelo más natural para LLMs

---

**Última actualización:** 20 de septiembre, 2025
**Versión actual:** 3.1 - Dataset de propiedades implementado
**Próximo hito:** Commit 3/16 - Obtener datos de servicios (guía urbana)

---

## Versión 3.0 - Implementación de Estructura del Proyecto
**Fecha:** 20 de septiembre, 2025
**Cambio Mayor:** Creación de la estructura base del sistema de recomendación

### Cambio de Enfoque
**Objetivo:** Transición desde la fase de planificación a la implementación concreta del sistema de recomendación para asesores comerciales.

### Implementación Técnica

#### Arquitectura del Sistema
- **Motor de Recomendación (`src/recommendation_engine.py`)**:
  - Algoritmo de matching con ponderación multifactorial
  - Sistema de compatibilidad (0-100%) basado en 5 factores
  - Generador automático de justificaciones para cada recomendación

#### Ponderación del Algoritmo
- **Presupuesto**: 30% - Evaluación de ajuste de precio
- **Composición Familiar**: 25% - Adecuación de espacio
- **Servicios Cercanos**: 20% - Proximidad a necesidades
- **Demografía**: 15% - Compatibilidad del área
- **Preferencias**: 10% - Ubicación y estilo de vida

#### Interfaz de Usuario (`src/cli.py`)
- **CLI con Typer + Rich**: Interfaz amigable con colores y tablas
- **Comandos principales**:
  - `recomendar`: Generar recomendaciones basadas en perfil
  - `listar-propiedades`: Mostrar propiedades disponibles
  - `ayuda`: Documentación y ejemplos de uso
- **Formatos de salida**: tabla, JSON, detallado
- **Soporte para perfiles**: Desde archivo JSON o descripción en texto

#### Stack Tecnológico Implementado
- **Python 3.11+**: Lenguaje principal
- **Pandas + NumPy**: Procesamiento de datos
- **Typer + Rich**: Interfaz de línea de comandos
- **OpenRouter/OpenAI**: Integración LLM (preparada)
- **Pytest**: Suite de pruebas completa

#### Calidad y Testing
- **Cobertura de pruebas**: 100% del motor de recomendación
- **Tests unitarios**: Evaluación de cada componente del algoritmo
- **Fixtures**: Datos de prueba consistentes y reutilizables
- **Validación**: Pruebas para diferentes tipos de perfiles

### Flujo de Desarrollo por Commits
Estructura organizada en 16 commits secuenciales:
- **Commits 1-4**: Preparación de datos y estructura OK: (Completado)
- **Commits 5-8**: Motor de recomendación (pendiente)
- **Commits 9-12**: Interfaz de usuario (pendiente)
- **Commits 13-16**: Validación y demo (pendiente)

### GitHub Projects Integration
- **Proyecto creado**: Sistema de Recomendación Inmobiliaria - PoC
- **Seguimiento visual**: Tablero Kanban con columnas y epics
- **Tareas organizadas**: 4 epics principales con 16 tareas totales
- **URL**: https://github.com/users/vincentiwadsworth/projects/1

### Cambios Específicos
1. **Eliminación de restricción offline**: Sistema ahora usa LLM para consultas en lenguaje natural
2. **Enfoque minimalista**: Sin Docker, priorizando simplicidad y velocidad
3. **Desarrollo paralelo**: Estructura adaptable para trabajo junto a empleo principal
4. **Calidad desde el inicio**: Testing completo y documentación integrada

### Próximos Pasos Inmediatos
- **Commit 2/16**: Preparar dataset de 5 propiedades en JSON
- **Commit 3/16**: Obtener y formatear datos de servicios (guía urbana)
- **Commit 4/16**: Crear 3 perfiles de prospecto ejemplo
- **Commit 5/16**: Implementar funciones específicas del algoritmo de matching

### Validaciones Realizadas
- [x] Estructura de proyecto funcional
- [x] Motor de recomendación básico operativo
- [x] CLI con comandos principales
- [x] Suite de pruebas completa
- [x] Documentación actualizada
- [x] GitHub Project configurado

---

**Versión anterior:** 3.0 - Estructura de proyecto implementada
**Nueva versión:** 3.1 - Dataset de propiedades implementado
**Estado:** Listo para continuar con Commit 3/16

---

## Versión 3.1 - Dataset de Propiedades Implementado
**Fecha:** 20 de septiembre, 2025
**Cambio Mayor:** Creación de dataset completo con 5 propiedades representativas

### Dataset de Propiedades Creado

#### Propiedades Incluidas
1. **Altos del Golf - Departamento 2D** ($185K)
   - 3 habitaciones, 2 baños, 120m²
   - Zona Norte, cerca de escuelas y supermercados
   - Ideal para familias con hijos

2. **Golden Tower - Studio 15A** ($95K)
   - 1 habitación, 1 baño, 45m²
   - Centro, cerca de universidades
   - Ideal para jóvenes profesionales y estudiantes

3. **Villa Magna - Casa 3B** ($320K)
   - 4 habitaciones, 3 baños, 180m²
   - Equipetrol, zona residencial premium
   - Ideal para familias establecidas

4. **Avanti Condominio - Dúplex 7C** ($145K)
   - 2 habitaciones, 2 baños, 85m²
   - 3er Anillo, opción accesible
   - Ideal para parejas jóvenes

5. **Inmoba Tower - Penthouse 20A** ($450K)
   - 3 habitaciones, 3 baños, 200m²
   - Centro, lujo y vistas panorámicas
   - Ideal para profesionales de alto nivel

#### Datos Completos por Propiedad
- **Características**: precio, habitaciones, baños, superficie, piso
- **Ubicación**: dirección exacta, barrio, coordenadas GPS
- **Servicios cercanos**: distancias a escuelas, supermercados, hospitales, universidades
- **Demografía**: nivel socioeconómico, composición familiar típica, seguridad

### Perfiles de Prospecto Creados

#### Perfil 1: Familia Martínez López
- **Composición**: 2 adultos + 2 niños (8 y 12 años)
- **Presupuesto**: $250-300K
- **Necesidades**: escuela_primaria, supermercado, hospital
- **Preferencias**: zona norte, seguridad alta

#### Perfil 2: Pareja Joven (Carlos y Sofía)
- **Composición**: 2 adultos profesionales
- **Presupuesto**: $180-220K
- **Necesidades**: universidad, supermercado, gimnasio
- **Preferencias**: centro, vida urbana

#### Perfil 3: Adulto Mayor (Roberto Silva)
- **Composición**: 1 adulto mayor jubilado
- **Presupuesto**: $120-160K
- **Necesidades**: hospital, supermercado, farmacia
- **Preferencias**: equipetrol, accesibilidad

### Script de Procesamiento

#### Funcionalidades Implementadas
- **Lector de Excel**: Maneja múltiples formatos (.xlsx, .xls)
- **Exploración de datos**: Identifica columnas relevantes automáticamente
- **Extracción inteligente**: Busca patrones en datos de Citrino
- **Dataset de ejemplo**: Propiedades realistas basadas en mercado SCZ

#### Procesamiento de Datos Reales
- Análisis de archivos consolidados de Citrino
- Identificación de zonas y proyectos
- Extracción de información de precios y características
- Generación de dataset estructurado JSON

### Validaciones Realizadas
- [x] Dataset de 5 propiedades con datos completos
- [x] 3 perfiles de prospecto representativos
- [x] Script de procesamiento de datos Citrino
- [x] Estructura JSON consistente y validada
- [x] Coordenadas geográficas reales de Santa Cruz
- [x] Servicios cercanos con distancias realistas

### Próximos Pasos
- **Commit 3/16**: Obtener y formatear datos de servicios (guía urbana)
- **Commit 4/16**: Validar y refinar perfiles de ejemplo
- **Commit 5/16**: Implementar funciones específicas del algoritmo
</smtcmp_block>