Basado en [[Propuesta de trabajo - Citrino - Integración de bases de datos 05#4. Enfoque de Trabajo]]
## inbox ideas
- [x] descargar información compartida por Franz
- [x] redactar plan operativo en detalle a partir de secciones del documento base
- [ ] integrar xlsx en VS Code
- [ ] generar listado de documentos usando VS Code 


---
# **Plan de Trabajo Detallado: Integración de Datos para Citrino**

## **Fase 1: Análisis y Diseño (Semanas 1-2)**
**Objetivo:** Traducir los requerimientos del negocio y la estructura de los archivos existentes en un plano técnico (arquitectura de base de datos) que sea robusto y escalable.

---

**Semana 1: Descubrimiento y Análisis Exploratorio de Datos**

*   **Tareas:**
    1. [x]  **Recepción y Análisis Inicial:** Solicitaré y recibiré el primer archivo clave: `Relevamiento de inmuebles residenciales 2012-2025 anualizado`.
			==Guardé en la carpeta Franz me compartió  en C:\Users\USER\Documents\Trabajo\Citrino\01 bases de datos\datos originales==
    2. [x]  **Perfilado de Datos (Data Profiling):** Usaré un script de Python (con la librería Pandas) para realizar un análisis automático del archivo. Este script generará un informe inicial que responderá a preguntas como:
        *   ¿Cuántas filas y columnas tiene?
        *   ¿Qué tipo de dato hay en cada columna (texto, número, fecha)?
        *   ¿Hay valores faltantes o nulos? ¿En qué columnas y con qué frecuencia?
        *   ¿Cuáles son los valores únicos en columnas clave (ej. tipos de propiedad, barrios)?
        ==Registré las entidades de cada archivo en C:Users/Obsidian/citrino/mapeo.md==
    3. [ ]  **Identificación de Entidades y Atributos:** Basado en el perfilado, comenzaremos a identificar las "cosas" o "conceptos" principales de tu negocio y sus características.

*   **Conceptos Clave (De Excel a Bases de Datos):**
    > **Entidad:** Piensa en una entidad como el tema principal de una hoja de cálculo. En lugar de tener un solo archivo gigante, en una base de datos separamos los temas. Por ejemplo, `Inmueble` es una entidad. `Barrio` es otra. `TipoDePropiedad` (Casa, Departamento) es otra.
    >
    > **Atributo:** Son las características de una entidad, es decir, las columnas de la tabla. Para la entidad `Inmueble`, los atributos serían `precio`, `direccion`, `cantidad_de_baños`, etc.

*   **Entregable de la Semana:**
    *   **Un resumen en Markdown con los hallazgos del perfilado de datos.**
    *   Una lista preliminar de las entidades y atributos identificados (Ej: Entidad `Inmueble` con atributos `precio`, `superficie`, etc.).
==Paco: terminé perfilado de entidades y atributos. tiempo de trabajo 2 horas== 

---

**Semana 2: Diseño del Esquema y la Arquitectura**

*   **Tareas:**
    1.  **Modelado de Datos (Creación del Diagrama Entidad-Relación):** Diseñaré un diagrama visual (ERD) que muestra las entidades como cajas y cómo se conectan entre sí. Esto es el plano de nuestra base de datos.
    2.  **Definición de Claves y Relaciones:** Estableceré las reglas para conectar las tablas.
    3.  **Normalización de la Base de Datos:** Aplicaré principios de diseño para evitar la redundancia y asegurar la integridad de los datos.
    4.  **Diseño del Esquema Físico:** Traduciré el diagrama ERD a código SQL (lenguaje de las bases de datos) que define la estructura de cada tabla, sus columnas y tipos de datos.

*   **Conceptos Clave (La Magia de lo "Relacional"):**
    > **Clave Primaria (Primary Key):** Es un identificador único para cada fila en una tabla, como el número de carnet de identidad para una persona. Ningún inmueble en nuestra tabla `Inmuebles` podrá tener el mismo ID. Esto garantiza que no haya duplicados.
    >
    > **Clave Foránea (Foreign Key):** Es el pegamento que une las tablas. Si tenemos una tabla `Inmuebles` y una tabla `Barrios`, la tabla `Inmuebles` no contendrá el nombre del barrio directamente. En su lugar, tendrá una columna `barrio_id` (la clave foránea) que apunta al ID único del barrio en la tabla `Barrios`.
    >
    > **Normalización:** Este es el proceso de organizar los datos para reducir la redundancia. En Excel, podrías escribir "Equipetrol Norte" 100 veces, con el riesgo de escribirlo mal ("Equipetrol N.") alguna vez. Con la normalización, "Equipetrol Norte" existe UNA SOLA VEZ en la tabla `Barrios` con un ID, digamos `5`. En la tabla `Inmuebles`, simplemente repetimos el número `5`. Esto ahorra espacio y, lo más importante, evita inconsistencias.

*   **Entregable de la Semana:**
    *   Diagrama Entidad-Relación (ERD) en formato de imagen.
    *   Documento Markdown explicando la estructura, las tablas y las relaciones definidas.
    *   Script SQL (`schema.sql`) con los comandos `CREATE TABLE` para construir la base de datos.

---

## **Fase 2: Implementación y Migración (Semanas 3-5)**
**Objetivo:** Construir la base de datos según el diseño y mover los datos desde los archivos de Google Sheets a su nuevo hogar estructurado, limpiándolos en el proceso.

---

**Semana 3: Construcción y Desarrollo de Scripts de Migración (ETL)**

*   **Tareas:**
    1.  **Creación de la Base de Datos:** Ejecutaré el script `schema.sql` para crear la estructura vacía de la base de datos en el entorno de desarrollo.
    2.  **Desarrollo del Script ETL:** Escribiré un script en Python que realice el proceso de **Extract, Transform, Load (Extraer, Transformar, Cargar)**.
        *   **Extract:** Leer los datos del archivo Google Sheets (`2012-2025 anualizado`).
        *   **Transform:** Aplicar reglas de limpieza. Ejemplos: convertir "2 baños" y "2 BAÑOS" a un número `2`; estandarizar direcciones; asegurar que las fechas tengan un formato consistente.
        *   **Load:** Insertar los datos limpios y transformados en las tablas correspondientes de la nueva base de datos SQL.

*   **Entregable de la Semana:**
    *   Un script de Python (`migrate_main_data.py`) documentado, listo para ser ejecutado.

---

**Semana 4-5: Migración, Validación e Integración de Fuentes Adicionales**

*   **Tareas:**
    1.  **Ejecución de la Migración Principal:** Correremos el script `migrate_main_data.py` para poblar la base de datos con los datos históricos.
    2.  **Validación de Datos:** Realizaremos comprobaciones para asegurar que la migración fue exitosa (ej. contar filas en el origen y destino, verificar sumas de columnas numéricas).
    3.  **Adaptación del Script ETL:** Modificaré el script para que sea compatible con las otras fuentes de datos (`Inmuebles en alquiler`, `Inmuebles usados`, `Guía urbana`).
    4.  **Migración de Fuentes Secundarias:** Ejecutaremos el script para cada una de las fuentes restantes.

*   **Concepto Clave (Proceso Replicable):**
    > La belleza de un buen script ETL es que es **reutilizable**. En lugar de empezar de cero para cada archivo, adaptamos el 80% del código existente. Esto acelera enormemente el trabajo y garantiza que las mismas reglas de limpieza y calidad se apliquen a todos tus datos, creando un conjunto de información unificado y consistente.

*   **Entregable de la Semana:**
    *   Base de datos poblada con todas las fuentes de datos proporcionadas.
    *   Informe de validación de la migración en Markdown.

---

## **Fase 3: Optimización y Entrega (Semanas 6-8)**
**Objetivo:** Asegurar que la base de datos no solo almacene los datos correctamente, sino que también sea rápida, segura y fácil de usar para herramientas externas como la IA.

---

**Semana 6: Pruebas de Rendimiento y Acondicionamiento para IA**

*   **Tareas:**
    1.  **Optimización de Consultas (Indexing):** Analizaré los tipos de preguntas que se harán a la base de datos y crearé "índices" en las columnas más consultadas (ej. precio, barrio, tipo de propiedad).
    2.  **Creación de Vistas (Views):** Para facilitar la conexión con la IA, crearé "vistas". Una vista es como una tabla virtual que presenta datos de múltiples tablas ya unidos y listos para consumir. Por ejemplo, una vista `inmuebles_completos` que ya contenga toda la información del inmueble junto con el nombre del barrio y el tipo de propiedad.

*   **Conceptos Clave (Velocidad y Simplicidad):**
    > **Índices (Indexes):** Un índice en una base de datos funciona exactamente como el índice de un libro. En lugar de leer todo el libro (escanear toda la tabla) para encontrar una información, la base de datos mira el índice y va directamente a la página correcta. Esto hace que las consultas sean órdenes de magnitud más rápidas.
    >
    > **Vistas (Views):** Una vista simplifica la complejidad. La IA no necesita saber cómo unir 5 tablas diferentes. Simplemente le pedimos que consulte la vista `inmuebles_completos`, que ya hemos preparado para ella. Es muy similar a cómo en Power BI creas una consulta en Power Query que une varias fuentes, y luego trabajas con el resultado final.

*   **Entregable de la Semana:**
    *   Scripts SQL con los comandos para crear los índices y las vistas.

---

**Semana 7-8: Documentación, Entrega y Capacitación**

*   **Tareas:**
    1.  **Documentación Técnica Final:** Consolidaré toda la documentación: el diagrama ERD, la descripción de cada tabla y columna, y el propósito de las vistas e índices.
    2.  **Implementación de Seguridad:** Me aseguraré de que los campos sensibles estén correctamente manejados.
    3.  **Sesión de Entrega y Capacitación (Handover):** Realizaremos una sesión donde te explicaré la arquitectura final, cómo acceder a los datos y cómo mantener el sistema. Te entregaré todos los scripts y la documentación.
    4.  **Cierre del Proyecto:** Finalización y entrega formal.

*   **Entregable Final del Proyecto:**
    *   Una base de datos centralizada, poblada, optimizada y segura.
    *   Un manual técnico completo en formato Markdown para tu bóveda de Obsidian.
    *   Todos los scripts (SQL y Python) utilizados en el proyecto.

---

**Próximo Paso Inmediato:**

Para dar inicio a la **Semana 1**, por favor, proporcióname acceso al archivo **"Relevamiento de inmuebles residenciales 2012-2025 anualizado"**. Puedes compartir una exportación en formato CSV o Excel. Con eso, generaré el primer análisis de perfilado de datos.