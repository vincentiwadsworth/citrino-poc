"""
Pruebas para el motor de recomendación.
"""

import pytest
import sys
import os

# Agregar el directorio src al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from recommendation_engine import RecommendationEngine


@pytest.fixture
def engine():
    """Fixture que proporciona una instancia del motor de recomendación."""
    return RecommendationEngine()


@pytest.fixture
def propiedades_ejemplo():
    """Fixture con propiedades de ejemplo para las pruebas."""
    return [
        {
            "id": "prop_001",
            "caracteristicas": {
                "precio": 280000,
                "habitaciones": 3,
                "banos": 2,
                "superficie": 120
            },
            "ubicacion": {
                "direccion": "Calle Norte 123",
                "barrio": "Norte",
                "coordenadas": {"lat": -34.5, "lng": -58.5}
            },
            "servicios_cercanos": {
                "escuela_primaria": [{"nombre": "Escuela Norte", "distancia": 300}],
                "supermercado": [{"nombre": "Super Norte", "distancia": 500}]
            }
        },
        {
            "id": "prop_002",
            "caracteristicas": {
                "precio": 195000,
                "habitaciones": 2,
                "banos": 1,
                "superficie": 80
            },
            "ubicacion": {
                "direccion": "Av. Central 456",
                "barrio": "Centro",
                "coordenadas": {"lat": -34.6, "lng": -58.4}
            },
            "servicios_cercanos": {
                "universidad": [{"nombre": "Universidad Metropolitana", "distancia": 400}],
                "supermercado": [{"nombre": "Super Centro", "distancia": 200}]
            }
        }
    ]


@pytest.fixture
def perfil_familia():
    """Fixture con perfil de una familia."""
    return {
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


@pytest.fixture
def perfil_pareja_joven():
    """Fixture con perfil de pareja joven."""
    return {
        "composicion_familiar": {
            "adultos": 2,
            "ninos": [],
            "adultos_mayores": 0
        },
        "presupuesto": {
            "min": 180000,
            "max": 220000,
            "tipo": "compra"
        },
        "necesidades": ["universidad", "supermercado"],
        "preferencias": {
            "ubicacion": "centro",
            "estilo_vida": "urbano"
        }
    }


class TestRecommendationEngine:
    """Clase de pruebas para el motor de recomendación."""

    def test_cargar_propiedades(self, engine, propiedades_ejemplo):
        """Prueba que las propiedades se cargan correctamente."""
        engine.cargar_propiedades(propiedades_ejemplo)
        assert len(engine.propiedades) == 2
        assert engine.propiedades[0]["id"] == "prop_001"

    def test_calcular_compatibilidad_familia(self, engine, propiedades_ejemplo, perfil_familia):
        """Prueba el cálculo de compatibilidad para perfil familiar."""
        engine.cargar_propiedades(propiedades_ejemplo)

        # Probar con la propiedad que coincide (Norte)
        compatibilidad = engine.calcular_compatibilidad(perfil_familia, propiedades_ejemplo[0])
        assert compatibilidad > 0
        assert compatibilidad <= 100

        # Probar con la propiedad que no coincide tanto (Centro)
        compatibilidad2 = engine.calcular_compatibilidad(perfil_familia, propiedades_ejemplo[1])
        assert compatibilidad > compatibilidad2  # La primera debe tener mejor compatibilidad

    def test_calcular_compatibilidad_pareja_joven(self, engine, propiedades_ejemplo, perfil_pareja_joven):
        """Prueba el cálculo de compatibilidad para perfil de pareja joven."""
        engine.cargar_propiedades(propiedades_ejemplo)

        # Para pareja joven, la propiedad del centro debe ser mejor
        compatibilidad_centro = engine.calcular_compatibilidad(perfil_pareja_joven, propiedades_ejemplo[1])
        compatibilidad_norte = engine.calcular_compatibilidad(perfil_pareja_joven, propiedades_ejemplo[0])
        assert compatibilidad_centro > compatibilidad_norte

    def test_evaluar_presupuesto(self, engine, perfil_familia):
        """Prueba la evaluación de presupuesto."""
        propiedad_correcta = {"caracteristicas": {"precio": 280000}}
        propiedad_barata = {"caracteristicas": {"precio": 200000}}
        propiedad_cara = {"caracteristicas": {"precio": 350000}}
        propiedad_muy_cara = {"caracteristicas": {"precio": 500000}}

        # Puntuación perfecta para precio en rango
        assert engine._evaluar_presupuesto(perfil_familia, propiedad_correcta) == 1.0

        # Puntuación reducida pero aceptable para precio debajo del mínimo
        assert engine._evaluar_presupuesto(perfil_familia, propiedad_barata) == 0.5

        # Puntuación parcial para precio ligeramente encima
        assert 0 < engine._evaluar_presupuesto(perfil_familia, propiedad_cara) < 1.0

        # Puntuación mínima para precio muy caro
        assert engine._evaluar_presupuesto(perfil_familia, propiedad_muy_cara) >= 0.2

    def test_evaluar_composicion_familiar(self, engine):
        """Prueba la evaluación de composición familiar."""
        perfil_familia_grande = {"composicion_familiar": {"adultos": 2, "ninos": [1, 2], "adultos_mayores": 0}}
        perfil_pareja = {"composicion_familiar": {"adultos": 2, "ninos": [], "adultos_mayores": 0}}

        propiedad_3_hab = {"caracteristicas": {"habitaciones": 3}}
        propiedad_1_hab = {"caracteristicas": {"habitaciones": 1}}

        # Familia grande necesita 3 habitaciones
        assert engine._evaluar_composicion_familiar(perfil_familia_grande, propiedad_3_hab) == 1.0
        assert engine._evaluar_composicion_familiar(perfil_familia_grande, propiedad_1_hab) < 1.0

        # Pareja necesita 1 habitación
        assert engine._evaluar_composicion_familiar(perfil_pareja, propiedad_1_hab) == 1.0

    def test_evaluar_servicios(self, engine):
        """Prueba la evaluación de servicios cercanos."""
        perfil = {"necesidades": ["escuela_primaria", "supermercado", "hospital"]}
        propiedad_buena = {
            "servicios_cercanos": {
                "escuela_primaria": [{"nombre": "Escuela", "distancia": 300}],
                "supermercado": [{"nombre": "Super", "distancia": 200}],
                "hospital": [{"nombre": "Hospital", "distancia": 1000}]
            }
        }
        propiedad_regular = {
            "servicios_cercanos": {
                "escuela_primaria": [{"nombre": "Escuela", "distancia": 300}],
                "supermercado": [{"nombre": "Super", "distancia": 200}]
            }
        }
        propiedad_mala = {"servicios_cercanos": {}}

        # Buena: todos los servicios disponibles
        assert engine._evaluar_servicios(perfil, propiedad_buena) == 1.0

        # Regular: 2 de 3 servicios disponibles
        assert engine._evaluar_servicios(perfil, propiedad_regular) == 2/3

        # Mala: ningún servicio disponible
        assert engine._evaluar_servicios(perfil, propiedad_mala) == 0.0

    def test_generar_recomendaciones(self, engine, propiedades_ejemplo, perfil_familia):
        """Prueba la generación de recomendaciones completas."""
        engine.cargar_propiedades(propiedades_ejemplo)
        recomendaciones = engine.generar_recomendaciones(perfil_familia, limite=5)

        # Debe retornar una lista
        assert isinstance(recomendaciones, list)

        # No debe exceder el límite
        assert len(recomendaciones) <= 5

        # Debe estar ordenada por compatibilidad (descendente)
        if len(recomendaciones) > 1:
            for i in range(len(recomendaciones) - 1):
                assert recomendaciones[i]['compatibilidad'] >= recomendaciones[i + 1]['compatibilidad']

        # Cada recomendación debe tener la estructura correcta
        for rec in recomendaciones:
            assert 'propiedad' in rec
            assert 'compatibilidad' in rec
            assert 'justificacion' in rec
            assert isinstance(rec['compatibilidad'], (int, float))
            assert 0 <= rec['compatibilidad'] <= 100

    def test_evaluar_demografia(self, engine):
        """Prueba la evaluación demográfica."""
        perfil_alto = {"presupuesto": {"max": 350000}, "composicion_familiar": {"adultos": 2, "ninos": [], "adultos_mayores": 0}}
        perfil_familia = {"presupuesto": {"max": 250000}, "composicion_familiar": {"adultos": 2, "ninos": [{"edad": 8}], "adultos_mayores": 0}}
        perfil_adulto_mayor = {"presupuesto": {"max": 180000}, "composicion_familiar": {"adultos": 1, "ninos": [], "adultos_mayores": 1}}

        propiedad_alta = {"demografia_area": {"nivel_socioeconomico": "alto", "composicion_familiar_tipica": "parejas_jovenes", "seguridad": "alta"}}
        propiedad_familiar = {"demografia_area": {"nivel_socioeconomico": "medio", "composicion_familiar_tipica": "familias", "seguridad": "media"}}
        propiedad_adultos_mayores = {"demografia_area": {"nivel_socioeconomico": "medio_bajo", "composicion_familiar_tipica": "adultos_mayores", "seguridad": "alta"}}

        # Perfil alto con propiedad alta - buena compatibilidad
        score_alto_alto = engine._evaluar_demografia(perfil_alto, propiedad_alta)
        assert score_alto_alto > 0.7

        # Perfil familia con propiedad familiar - buena compatibilidad
        score_familia_familiar = engine._evaluar_demografia(perfil_familia, propiedad_familiar)
        assert score_familia_familiar > 0.6

        # Perfil adulto mayor con propiedad para adultos mayores - buena compatibilidad
        score_adulto_adulto = engine._evaluar_demografia(perfil_adulto_mayor, propiedad_adultos_mayores)
        assert score_adulto_adulto >= 0.6

        # Prueba niveles socioeconómicos compatibles
        score_medio_alto = engine._evaluar_demografia(perfil_alto, propiedad_familiar)
        assert score_medio_alto > 0.1  # Debe tener alguna compatibilidad

        # Propiedad sin datos demográficos
        propiedad_sin_datos = {}
        score_sin_datos = engine._evaluar_demografia(perfil_familia, propiedad_sin_datos)
        assert score_sin_datos == 0.7  # Valor por defecto

    def test_evaluar_preferencias(self, engine):
        """Prueba la evaluación de preferencias de ubicación y estilo de vida."""
        perfil_norte = {"preferencias": {"ubicacion": "norte", "seguridad": "alta"}}
        perfil_centro = {"preferencias": {"ubicacion": "centro", "estilo_propiedad": "apartamento"}}
        perfil_caracteristicas = {"preferencias": {"caracteristicas_deseadas": ["amoblado", "espacioso"]}}

        propiedad_norte = {
            "ubicacion": {"barrio": "Norte", "zona": "Norte"},
            "caracteristicas": {"amoblado": True, "superficie": 120},
            "demografia_area": {"seguridad": "alta"}
        }
        propiedad_centro = {
            "ubicacion": {"barrio": "Centro Histórico", "zona": "Centro"},
            "tipo": "apartamento",
            "demografia_area": {"seguridad": "media"}
        }
        propiedad_no_preferida = {
            "ubicacion": {"barrio": "Sur", "zona": "Sur"},
            "caracteristicas": {"amoblado": False, "superficie": 80},
            "demografia_area": {"seguridad": "baja"}
        }

        # Preferencia de ubicación norte
        score_norte = engine._evaluar_preferencias(perfil_norte, propiedad_norte)
        assert score_norte >= 0.5

        # Preferencia de ubicación centro
        score_centro = engine._evaluar_preferencias(perfil_centro, propiedad_centro)
        assert score_centro > 0.5

        # Preferencia de características
        score_caracteristicas = engine._evaluar_preferencias(perfil_caracteristicas, propiedad_norte)
        assert score_caracteristicas >= 0.2  # amoblado + espacioso

        # Sin preferencias que coincidan
        score_no_preferencia = engine._evaluar_preferencias(perfil_norte, propiedad_no_preferida)
        assert score_no_preferencia < 0.5

    def test_determinar_nivel_socioeconomico(self, engine):
        """Prueba la determinación de nivel socioeconómico basado en presupuesto."""
        perfil_alto = {"presupuesto": {"max": 350000}}
        perfil_medio_alto = {"presupuesto": {"max": 250000}}
        perfil_medio = {"presupuesto": {"max": 150000}}
        perfil_bajo = {"presupuesto": {"max": 100000}}

        assert engine._determinar_nivel_socioeconomico(perfil_alto) == "alto"
        assert engine._determinar_nivel_socioeconomico(perfil_medio_alto) == "medio_alto"
        assert engine._determinar_nivel_socioeconomico(perfil_medio) == "medio"
        assert engine._determinar_nivel_socioeconomico(perfil_bajo) == "bajo"

    def test_son_niveles_compatibles(self, engine):
        """Prueba la compatibilidad entre niveles socioeconómicos."""
        # Niveles compatibles
        assert engine._son_niveles_compatibles("alto", "medio_alto") == True
        assert engine._son_niveles_compatibles("medio", "bajo") == True
        assert engine._son_niveles_compatibles("alto", "alto") == True

        # Niveles no compatibles
        assert engine._son_niveles_compatibles("alto", "bajo") == False
        assert engine._son_niveles_compatibles("medio", "alto") == False

    def test_pesos_correctos(self, engine):
        """Prueba que los pesos de los factores suman 1.0."""
        total_pesos = sum(engine.pesos.values())
        assert abs(total_pesos - 1.0) < 0.001

        # Verificar pesos individuales
        assert engine.pesos['presupuesto'] == 0.30
        assert engine.pesos['composicion_familiar'] == 0.25
        assert engine.pesos['servicios'] == 0.20
        assert engine.pesos['demografia'] == 0.15
        assert engine.pesos['preferencias'] == 0.10

    def test_justificacion_contiene_informacion_relevante(self, engine, propiedades_ejemplo, perfil_familia):
        """Prueba que la justificación contiene información relevante."""
        engine.cargar_propiedades(propiedades_ejemplo)
        recomendaciones = engine.generar_recomendaciones(perfil_familia, limite=1)

        if recomendaciones:
            justificacion = recomendaciones[0]['justificacion']
            assert "Compatibilidad:" in justificacion
            assert "Precio:" in justificacion
            assert "habitaciones" in justificacion.lower() or "Habitaciones:" in justificacion
            # Verificar que contiene factores de compatibilidad
            assert "Factores de compatibilidad:" in justificacion
            assert "Presupuesto:" in justificacion
            assert "Espacio:" in justificacion

    def test_generar_recomendaciones_sin_propiedades(self, engine, perfil_familia):
        """Prueba el comportamiento cuando no hay propiedades cargadas."""
        recomendaciones = engine.generar_recomendaciones(perfil_familia)
        assert isinstance(recomendaciones, list)
        assert len(recomendaciones) == 0

    def test_perfil_vacio(self, engine, propiedades_ejemplo):
        """Prueba el comportamiento con perfiles vacíos."""
        engine.cargar_propiedades(propiedades_ejemplo)
        perfil_vacio = {}

        recomendaciones = engine.generar_recomendaciones(perfil_vacio)
        # Debe manejar el caso sin errores
        assert isinstance(recomendaciones, list)

    def test_compatibilidad_siempre_en_rango(self, engine, propiedades_ejemplo):
        """Prueba que la compatibilidad siempre está en el rango 0-100."""
        engine.cargar_propiedades(propiedades_ejemplo)

        # Probar con diferentes perfiles
        perfiles_prueba = [
            {"presupuesto": {"min": 1000, "max": 5000}, "composicion_familiar": {"adultos": 1}},
            {"presupuesto": {"min": 1000000, "max": 2000000}, "composicion_familiar": {"adultos": 5, "ninos": [{"edad": 10}, {"edad": 12}]}},
            {}  # Perfil vacío
        ]

        for perfil in perfiles_prueba:
            for propiedad in propiedades_ejemplo:
                compatibilidad = engine.calcular_compatibilidad(perfil, propiedad)
                assert 0 <= compatibilidad <= 100, f"Compatibilidad fuera de rango: {compatibilidad}"

    def test_servicios_con_necesidades_vacias(self, engine):
        """Prueba evaluación de servicios cuando no hay necesidades específicas."""
        perfil_sin_necesidades = {"necesidades": []}
        propiedad_con_servicios = {
            "servicios_cercanos": {
                "escuela_primaria": [{"nombre": "Escuela", "distancia": 300}],
                "supermercado": [{"nombre": "Super", "distancia": 200}]
            }
        }

        score = engine._evaluar_servicios(perfil_sin_necesidades, propiedad_con_servicios)
        assert score == 0.5  # Valor por defecto cuando no hay necesidades

    def test_composicion_familiar_sin_datos(self, engine):
        """Prueba evaluación de composición familiar cuando faltan datos."""
        perfil_incompleto = {"composicion_familiar": {}}
        propiedad_sin_habitaciones = {"caracteristicas": {}}

        score = engine._evaluar_composicion_familiar(perfil_incompleto, propiedad_sin_habitaciones)
        assert score == 0.0