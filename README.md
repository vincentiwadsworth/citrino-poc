# Citrino - Sistema de Recomendación Inmobiliaria

## 🏠 Sistema Inteligente de Recomendación con Geolocalización Real

### **Visión del Proyecto**
Citrino es un sistema avanzado de recomendación inmobiliaria que utiliza inteligencia artificial, geolocalización precisa y datos municipales para Santa Cruz de la Sierra.

### **Estadísticas Actuales**
- **Total Propiedades**: 76,853 con coordenadas exactas
- **Servicios Urbanos**: 4,777 puntos georreferenciados
- **Proyectos de Inteligencia**: 323 con análisis exclusivos
- **Precisión de Recomendación**: 85-96% (vs 73% constante anterior)
- **Motor de Recomendación**: 100% efectividad

## **🚀 Inicio Rápido**

### Para Reuniones y Demostraciones (Recomendado)
```bash
# Verificar estado del sistema
python verificar_servicios.py

# Iniciar todo automáticamente
./iniciar_demo.bat

# Acceder a la demo: http://localhost:8501
```

### Instalación Manual
```bash
# 1. Instalar dependencias
pip install -r requirements_api.txt

# 2. Iniciar API
python api/server.py

# 3. Ejecutar demo (estable para reuniones)
streamlit run demo_stable.py
```

## **🎯 Características Principales**

### Motor de Recomendación Avanzado
- 🎯 **Algoritmo Multi-factor**: Presupuesto (25%), Familia (20%), Servicios (30%), Demografía (15%), Preferencias (10%)
- 🗺️ **Geolocalización Real**: Cálculo exacto de distancias con fórmula Haversine
- ⚡ **Optimización Inteligente**: 99.3% mejora en rendimiento con pre-filtrado por zonas
- 📊 **Precisión Mejorada**: 85-96% compatibilidad basada en distancia real a servicios

### Integración de Datos Municipales
- 🏛️ **Guía Urbana Completa**: 4,777 servicios georreferenciados en 6 categorías
- 🎓 **Mapeo de Necesidades**: Convierte necesidades genéricas en servicios específicos
- 📍 **Indexación Espacial**: Búsqueda eficiente de servicios cercanos
- 🔄 **Actualización Automática**: Integración con datos municipales oficiales

### Sistema de Demostración Profesional
- 🏠 **Interfaz Moderna**: Welcome screen, diseño responsive, UX profesional
- 👥 **Perfiles Diversos**: 6 tipos diferentes de prospectos (familias, inversores, profesionales)
- 🔧 **Herramientas de Reunión**: Verificación automática, inicio con un clic, guía de emergencia
- 📱 **Estabilidad Mejorada**: Versión simplificada para máxima fiabilidad

### Herramientas Técnicas
- 🌐 **API REST Completa**: Endpoints para recomendaciones originales y mejoradas
- 🧪 **Sistema de Verificación**: Diagnóstico automático de servicios y conexión
- 📈 **Monitoreo en Tiempo Real**: Health checks, métricas de rendimiento
- 🛠️ **Scripts Automatizados**: Inicio, verificación y recuperación automática

## **📁 Estructura del Proyecto**

```
citrino/
├── 🚀 Archivos Principales (Sistema y Demo)
│   ├── demo_stable.py                    # Demo estable para reuniones
│   ├── demo_con_geolocalizacion.py       # Demo completa con geolocalización
│   ├── iniciar_demo.bat                  # Script de inicio automático
│   ├── verificar_servicios.py            # Sistema de verificación y diagnóstico
│   └── instrucciones_reunion.txt         # Guía de emergencia para reuniones
│
├── 🔧 Sistema (api/, src/, data/, scripts/, tests/) # Código fuente
│   ├── api/server.py                     # API REST con Flask
│   ├── src/recommendation_engine*.py     # Motores de recomendación
│   ├── data/                             # Bases de datos (76,853 propiedades)
│   └── scripts/                          # Scripts de evaluación y procesamiento
│
└── 📚 documentation/                     # Documentación organizada
    ├── ALGORITMO_HAVERSINE.md           # Documentación técnica del algoritmo
    ├── evaluacion/                      # Informes completos de evaluación
    ├── planes_futuros/                  # Planes futuros (wiki, roadmap)
    └── obsoleto/                        # Archivos obsoletos o de backup
```

## **📝 Documentación y Recursos**

### Documentación Técnica
- **`documentation/ALGORITMO_HAVERSINE.md`**: Algoritmo de geolocalización y optimización
- **`documentation/evaluacion/INFORME_EVALUACION_SISTEMA_COMPLETO.md`**: Evaluación completa del sistema

### Herramientas para Reuniones
- **`instrucciones_reunion.txt`**: Guía paso a paso para emergencias
- **`verificar_servicios.py`**: Diagnóstico automático del sistema (API + Streamlit)

### Planes Futuros
- **`documentation/planes_futuros/WIKI_IMPLEMENTACION_FUTURA.md`**: Plan para wiki centralizada de conocimiento

---

## **🎯 Backlog del Proyecto - Funcionalidades Futuras**

### **🚀 Próximas Prioridades (Corto Plazo)**
- [ ] **Mejora de calidad de datos**: Reparar 46.6% de zonas corruptas
- [ ] **Sistema de validación automática**: Implementar controles de calidad en tiempo real
- [ ] **Deduplicación inteligente**: Eliminar duplicados entre fuentes Franz y scraping
- [ ] **Dashboard de monitoreo**: Calidad de datos y rendimiento del sistema

### **💡 Funcionalidades Comerciales (Mediano Plazo)**
- [ ] **Integración con WhatsApp**: Enviar briefings automáticamente
- [ ] **Módulo de valoración automática**: Precios de mercado por zona
- [ ] **Sistema de seguimiento de prospectos**: Pipeline comercial completo
- [ ] **Comparador de propiedades**: Análisis lado a lado
- [ ] **Alertas de nuevas propiedades**: Notificaciones por preferencias

### **🔧 Funcionalidades Técnicas (Mediano Plazo)**
- [ ] **App móvil para asesores**: Acceso móvil al sistema
- [ ] **Integración con portales**: Importación/exportación automática
- [ ] **Sistema de caché avanzado**: Mejorar rendimiento
- [ ] **API de reporting**: Reportes personalizados
- [ ] **Sistema de backup automático**: Resiliencia de datos

### **🎯 Funcionalidades Avanzadas (Largo Plazo)**
- [ ] **Motor de predicción de precios**: IA para valoración futura
- [ ] **Análisis de inversión**: ROI, cashflow, plusvalía
- [ ] **Integración con mapas interactivos**: Visualización geográfica
- [ ] **Sistema de recomendación de inversión**: Perfiles de riesgo
- [ ] **Marketplace digital**: Plataforma completa para transacciones

### **🏢 Funcionalidades Empresariales**
- [ ] **Módulo de gerencia**: Dashboard ejecutivo
- [ ] **Sistema de comisiones**: Automatización de cálculos
- [ ] **CRM integrado**: Gestión de relaciones con clientes
- [ ] **Reportes financieros**: Análisis de rendimiento
- [ ] **Sistema de seguridad avanzada**: Roles y permisos

---

## **Tecnología**
- **Backend**: Python + Flask + Pandas
- **Base de Datos**: JSON (actual) + PostgreSQL (futuro)
- **Frontend**: API REST para integraciones
- **IA**: Motor de recomendación propio
- **Scraping**: Web scraping automatizado

---

**Citrino Transformación Digital**
*Integrando datos, creando valor*

## **🎯 Estado Actual del Sistema**

### ✅ Funcionalidades Completadas
- ✅ **Base de datos consolidada**: 76,853 propiedades con coordenadas exactas
- ✅ **Motor de recomendación mejorado**: Geolocalización real con Haversine
- ✅ **Integración municipal**: 4,777 servicios urbanos georreferenciados
- ✅ **API REST completa**: Endpoints para motores original y mejorado
- ✅ **Sistema de demostración**: Interface profesional con 6 perfiles de prospectos
- ✅ **Herramientas de reunión**: Verificación automática y guía de emergencia
- ✅ **Evaluación completa**: 10 prospectos testeados con 100% éxito

### 🔄 En Progreso
- 🔄 **Optimización continua**: Mejora de rendimiento y estabilidad
- 🔄 **Documentación técnica**: Algoritmos y arquitectura del sistema

### 📋 Próximos Pasos
- 📋 **Wiki centralizada**: Documentación unificada para todo el equipo
- 📋 **Hosting gratuito**: Despliegue en Streamlit Cloud para acceso externo
- 📋 **Integración con LLM**: Consultas en lenguaje natural
- 📋 **Mejora de calidad**: Validación y deduplicación de datos
