#!/usr/bin/env python3
"""
Demo simple para reunión mañana - Streamlit
Muestra la API Citrino sin complejidad de LLM
"""

import streamlit as st
import requests
import json

# Configuración
API_URL = "http://localhost:5000"

st.set_page_config(
    page_title="Citrino API Demo",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Citrino API Demo")
st.markdown("Consulta 76,853 propiedades en tiempo real")

# Sidebar para controles
st.sidebar.header("Filtros de Búsqueda")

# Filtros básicos
presupuesto_max = st.sidebar.slider(
    "Presupuesto Máximo (USD)",
    min_value=50000,
    max_value=1000000,
    value=300000,
    step=10000
)

zona = st.sidebar.selectbox(
    "Zona",
    ["Todas", "Equipetrol", "Las Palmas", "Zona Norte", "Urubó", "Centro"]
)

tipo_propiedad = st.sidebar.selectbox(
    "Tipo de Propiedad",
    ["Todas", "departamento", "casa", "terreno"]
)

habitaciones_min = st.sidebar.slider(
    "Habitaciones Mínimas",
    min_value=1,
    max_value=6,
    value=2
)

# Botón de búsqueda
if st.sidebar.button("Buscar Propiedades", type="primary"):
    # Preparar parámetros
    params = {
        "precio_max": presupuesto_max,
        "limite": 10
    }

    if zona != "Todas":
        params["zona"] = zona
    if tipo_propiedad != "Todas":
        params["tipo_propiedad"] = tipo_propiedad
    if habitaciones_min > 1:
        params["habitaciones_min"] = habitaciones_min

    # Hacer petición
    try:
        with st.spinner("Buscando propiedades..."):
            response = requests.post(
                f"{API_URL}/api/buscar",
                json=params,
                timeout=30
            )

            if response.status_code == 200:
                resultado = response.json()

                if resultado.get('success'):
                    propiedades = resultado.get('propiedades', [])

                    # Mostrar resultados
                    st.success(f"Se encontraron {len(propiedades)} propiedades")

                    # Mostrar cada propiedad
                    for prop in propiedades:
                        with st.expander(f"🏠 {prop['nombre']} - ${prop['precio']:,}"):
                            col1, col2 = st.columns(2)

                            with col1:
                                st.write(f"**Ubicación:** {prop['zona']}")
                                st.write(f"**Superficie:** {prop['superficie_m2']} m²")
                                st.write(f"**Habitaciones:** {prop['habitaciones']}")
                                st.write(f"**Baños:** {prop['banos']}")

                            with col2:
                                st.write(f"**Garaje:** {'Sí' if prop['garaje'] else 'No'}")
                                st.write(f"**Fuente:** {prop['fuente']}")
                                if prop.get('espacios_garaje'):
                                    st.write(f"**Espacios Garage:** {prop['espacios_garaje']}")

                            if prop.get('descripcion'):
                                st.write(f"**Descripción:** {prop['descripcion'][:200]}...")

                else:
                    st.error(f"Error: {resultado.get('error', 'Error desconocido')}")

            else:
                st.error(f"Error HTTP: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("❌ No se puede conectar al servidor API")
        st.code("""
# Asegúrate de que el servidor esté corriendo:
cd api
python server.py
        """)
    except Exception as e:
        st.error(f"Error inesperado: {str(e)}")

# Sección de recomendaciones
st.header("🎯 Sistema de Recomendación")

st.subheader("Ejemplo: Familia Joven en Equipetrol")
st.code("""
Perfil:
- Presupuesto: $150,000 - $250,000
- Ubicación: Equipetrol
- Tipo: Departamento
- Familia: 2 adultos, 1 niño
- Necesidades: Seguridad, estacionamiento, áreas comunes
""", language="markdown")

if st.button("Generar Recomendación", key="recomendacion"):
    perfil = {
        "id": "demo_familia_joven",
        "presupuesto_min": 150000,
        "presupuesto_max": 250000,
        "adultos": 2,
        "ninos": [1],
        "adultos_mayores": 0,
        "zona_preferida": "Equipetrol",
        "tipo_propiedad": "departamento",
        "necesidades": ["seguridad", "estacionamiento", "areas_comunes"],
        "limite": 5,
        "umbral_minimo": 0.3
    }

    try:
        with st.spinner("Generando recomendaciones..."):
            response = requests.post(
                f"{API_URL}/api/recomendar",
                json=perfil,
                timeout=30
            )

            if response.status_code == 200:
                resultado = response.json()

                if resultado.get('success'):
                    recomendaciones = resultado.get('recomendaciones', [])

                    st.success(f"Se generaron {len(recomendaciones)} recomendaciones")

                    for rec in recomendaciones:
                        st.info(f"""
                        **{rec['nombre']}** - ${rec['precio']:,}
                        - **Compatibilidad:** {rec['compatibilidad']}%
                        - **Ubicación:** {rec['zona']}
                        - **Características:** {rec['habitaciones']} hab, {rec['banos']} baños, {rec['superficie_m2']} m²
                        - **Justificación:** {rec['justificacion']}
                        """)

                else:
                    st.error(f"Error: {resultado.get('error', 'Error desconocido')}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Instrucciones:**")
st.sidebar.markdown("1. Iniciar servidor API")
st.sidebar.markdown("2. Ajustar filtros")
st.sidebar.markdown("3. Click en 'Buscar'")
st.sidebar.markdown("\n**Servidor:**")
st.sidebar.code("cd api && python server.py")

# Health check
if st.sidebar.button("Verificar Estado API"):
    try:
        response = requests.get(f"{API_URL}/api/health", timeout=5)
        if response.status_code == 200:
            health = response.json()
            st.sidebar.success(f"✅ API Activa\nPropiedades: {health.get('total_propiedades', 0):,}")
        else:
            st.sidebar.error("❌ API no responde")
    except:
        st.sidebar.error("❌ No se puede conectar")