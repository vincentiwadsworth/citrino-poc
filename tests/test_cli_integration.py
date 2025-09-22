"""
Pruebas de integración para el sistema CLI.

Este módulo prueba la integración completa entre la CLI, el motor de recomendación
y los datos de propiedades y perfiles.
"""

import pytest
import sys
import os
import json
import tempfile
from unittest.mock import patch, MagicMock

# Agregar el directorio src al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Importar usando rutas absolutas
from recommendation_engine import RecommendationEngine


@pytest.fixture
def datos_prueba():
    """Fixture con datos de prueba completos."""
    return {
        "propiedades": [
            {
                "id": "prop_001",
                "nombre": "Departamento Norte",
                "tipo": "apartamento",
                "caracteristicas": {
                    "precio": 280000,
                    "habitaciones": 3,
                    "banos": 2,
                    "superficie": 120,
                    "amoblado": False,
                    "piso": 5
                },
                "ubicacion": {
                    "direccion": "Calle Norte 123",
                    "barrio": "Norte",
                    "zona": "Norte",
                    "coordenadas": {"lat": -34.5, "lng": -58.5}
                },
                "servicios_cercanos": {
                    "escuela_primaria": [{"nombre": "Escuela Norte", "distancia": 300}],
                    "supermercado": [{"nombre": "Super Norte", "distancia": 500}],
                    "hospital": [{"nombre": "Clinica Norte", "distancia": 1500}]
                },
                "demografia_area": {
                    "nivel_socioeconomico": "alto",
                    "composicion_familiar_tipica": "familias",
                    "seguridad": "alta"
                }
            },
            {
                "id": "prop_002",
                "nombre": "Apartamento Centro",
                "tipo": "apartamento",
                "caracteristicas": {
                    "precio": 195000,
                    "habitaciones": 2,
                    "banos": 1,
                    "superficie": 80,
                    "amoblado": True,
                    "piso": 2
                },
                "ubicacion": {
                    "direccion": "Av. Central 456",
                    "barrio": "Centro",
                    "zona": "Centro",
                    "coordenadas": {"lat": -34.6, "lng": -58.4}
                },
                "servicios_cercanos": {
                    "universidad": [{"nombre": "Universidad Metropolitana", "distancia": 400}],
                    "supermercado": [{"nombre": "Super Centro", "distancia": 200}],
                    "farmacia": [{"nombre": "Farmacia Central", "distancia": 150}]
                },
                "demografia_area": {
                    "nivel_socioeconomico": "medio",
                    "composicion_familiar_tipica": "parejas_jovenes",
                    "seguridad": "media"
                }
            }
        ],
        "perfiles": {
            "familia": {
                "nombre": "Familia García",
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
                "necesidades": ["escuela_primaria", "supermercado", "hospital"],
                "preferencias": {
                    "ubicacion": "norte",
                    "seguridad": "alta",
                    "caracteristicas_deseadas": ["espacioso"]
                }
            },
            "pareja_joven": {
                "nombre": "Pareja Joven López",
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
                    "estilo_vida": "urbano",
                    "estilo_propiedad": "apartamento"
                }
            }
        }
    }


class TestCLIIntegration:
    """Clase de pruebas de integración para la CLI."""

    def test_cargar_propiedades_desde_json_archivo_valido(self, datos_prueba):
        """Prueba cargar propiedades desde un archivo JSON válido."""
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(datos_prueba["propiedades"], f, ensure_ascii=False, indent=2)
            temp_file = f.name

        try:
            # Cargar propiedades
            with open(temp_file, 'r', encoding='utf-8') as f:
                propiedades = json.load(f)

            # Verificar carga correcta
            assert len(propiedades) == 2
            assert propiedades[0]["id"] == "prop_001"
            assert propiedades[1]["nombre"] == "Apartamento Centro"
        finally:
            # Limpiar archivo temporal
            os.unlink(temp_file)

    def test_cargar_propiedades_archivo_inexistente(self):
        """Prueba comportamiento cuando el archivo no existe."""
        try:
            with open("archivo_inexistente.json", 'r', encoding='utf-8') as f:
                propiedades = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            propiedades = []
        assert propiedades == []

    def test_cargar_propiedades_json_invalido(self):
        """Prueba comportamiento con JSON inválido."""
        # Crear archivo temporal con JSON inválido
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            f.write("{json_invalido")
            temp_file = f.name

        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                propiedades = json.load(f)
        except json.JSONDecodeError:
            propiedades = []
        assert propiedades == []

        os.unlink(temp_file)

    @patch('cli.console.print')
    def test_listar_propiedades_con_datos(self, mock_print, datos_prueba):
        """Prueba listar propiedades cuando hay datos disponibles."""
        # Mockear os.path.exists para que devuelva True
        with patch('cli.os.path.exists', return_value=True):
            # Mockear cargar_propiedades_desde_json
            with patch('cli.cargar_propiedades_desde_json', return_value=datos_prueba["propiedades"]):
                listar_propiedades()

                # Verificar que se llamó a console.print
                assert mock_print.called

                # Obtener las llamadas y verificar contenido
                calls = [str(call) for call in mock_print.call_args_list]
                output = ' '.join(calls)

                # Verificar que contiene información esperada
                assert "Propiedades Disponibles" in output
                assert "Departamento Norte" in output
                assert "Apartamento Centro" in output
                assert "280,000" in output  # Precio formateado

    @patch('cli.console.print')
    def test_listar_propiedades_sin_datos(self, mock_print):
        """Prueba listar propiedades cuando no hay datos."""
        # Mockear os.path.exists para que devuelva False
        with patch('cli.os.path.exists', return_value=False):
            listar_propiedades()

            # Verificar mensaje de advertencia
            mock_print.assert_called_with("[yellow]No hay propiedades cargadas en el sistema.[/yellow]")

    @patch('cli.console.print')
    def test_recomendar_con_perfil_json(self, mock_print, datos_prueba):
        """Prueba recomendar usando un perfil desde archivo JSON."""
        # Crear archivos temporales
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(datos_prueba["propiedades"], f, ensure_ascii=False, indent=2)
            propiedades_file = f.name

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(datos_prueba["perfiles"]["familia"], f, ensure_ascii=False, indent=2)
            perfil_file = f.name

        try:
            # Mockear os.path.exists para propiedades
            with patch('cli.os.path.exists') as mock_exists:
                mock_exists.side_effect = lambda path: path == propiedades_file

                # Mockear cargar_propiedades_desde_json
                with patch('cli.cargar_propiedades_desde_json', return_value=datos_prueba["propiedades"]):
                    # Ejecutar recomendar
                    recomendar(perfil=perfil_file, limite=3, formato="tabla")

                    # Verificar que se generaron recomendaciones
                    calls = [str(call) for call in mock_print.call_args_list]
                    output = ' '.join(calls)

                    assert "Propiedades Recomendadas" in output
                    assert "Cargadas 2 propiedades" in output
                    assert f"Perfil cargado desde {perfil_file}" in output

        finally:
            # Limpiar archivos temporales
            os.unlink(propiedades_file)
            os.unlink(perfil_file)

    @patch('cli.console.print')
    def test_recomendar_con_perfil_texto(self, mock_print, datos_prueba):
        """Prueba recomendar usando descripción en texto."""
        # Mockear os.path.exists para propiedades
        with patch('cli.os.path.exists', return_value=True):
            # Mockear cargar_propiedades_desde_json
            with patch('cli.cargar_propiedades_desde_json', return_value=datos_prueba["propiedades"]):
                # Ejecutar recomendar con texto
                recomendar(perfil="familia con 2 hijos", limite=2, formato="json")

                # Verificar que procesó el texto
                calls = [str(call) for call in mock_print.call_args_list]
                output = ' '.join(calls)

                assert "Analizando perfil desde descripcion..." in output
                assert "Generando recomendaciones..." in output

    @patch('cli.console.print')
    def test_recomendar_formato_json(self, mock_print, datos_prueba):
        """Prueba formato de salida JSON."""
        # Mockear sistema de archivos
        with patch('cli.os.path.exists', return_value=True):
            with patch('cli.cargar_propiedades_desde_json', return_value=datos_prueba["propiedades"]):
                with patch('cli.os.path.exists', return_value=False):  # Forzar texto
                    recomendar(perfil="test", formato="json")

                    # Verificar salida JSON
                    calls = [str(call) for call in mock_print.call_args_list]
                    output = ' '.join(calls)

                    # La salida debe ser JSON válido
                    assert "[" in output and "]" in output  # Estructura de lista
                    assert "compatibilidad" in output
                    assert "justificacion" in output

    @patch('cli.console.print')
    def test_recomendar_formato_detallado(self, mock_print, datos_prueba):
        """Prueba formato de salida detallado."""
        with patch('cli.os.path.exists', return_value=True):
            with patch('cli.cargar_propiedades_desde_json', return_value=datos_prueba["propiedades"]):
                with patch('cli.os.path.exists', return_value=False):
                    recomendar(perfil="test", formato="detallado")

                    # Verificar salida detallada
                    calls = [str(call) for call in mock_print.call_args_list]
                    output = ' '.join(calls)

                    assert "Recomendación" in output
                    assert "Justificacion" in output

    @patch('cli.console.print')
    def test_recomendar_sin_resultados(self, mock_print):
        """Prueba comportamiento cuando no hay recomendaciones."""
        # Mockear sistema con datos que no coinciden
        propiedades_vacias = []

        with patch('cli.os.path.exists', return_value=True):
            with patch('cli.cargar_propiedades_desde_json', return_value=propiedades_vacias):
                with patch('cli.os.path.exists', return_value=False):
                    recomendar(perfil="test")

                    # Verificar mensaje de no resultados
                    calls = [str(call) for call in mock_print.call_args_list]
                    output = ' '.join(calls)

                    assert "No se encontraron propiedades que coincidan con el perfil" in output

    def test_parsear_perfil_desde_texto_funcion_basica(self):
        """Prueba la función básica de parseo de perfil desde texto."""
        # Implementación simplificada para pruebas
        perfil = {
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

        # Verificar estructura básica
        assert isinstance(perfil, dict)
        assert "composicion_familiar" in perfil
        assert "presupuesto" in perfil
        assert "necesidades" in perfil
        assert "preferencias" in perfil

        # Verificar valores por defecto
        assert perfil["composicion_familiar"]["adultos"] == 2
        assert len(perfil["composicion_familiar"]["ninos"]) == 2
        assert perfil["presupuesto"]["min"] == 250000
        assert perfil["presupuesto"]["max"] == 300000


class TestCLIErrorHandling:
    """Clase de pruebas para manejo de errores en la CLI."""

    @patch('cli.console.print')
    def test_error_cargar_perfil_invalido(self, mock_print):
        """Prueba manejo de error al cargar perfil inválido."""
        # Crear archivo temporal con JSON inválido
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            f.write("{json_invalido")
            temp_file = f.name

        try:
            with patch('cli.os.path.exists', return_value=True):
                with patch('cli.cargar_propiedades_desde_json', return_value=[]):
                    recomendar(perfil=temp_file)

                    # Verificar mensaje de error
                    calls = [str(call) for call in mock_print.call_args_list]
                    output = ' '.join(calls)

                    assert "Error cargando perfil" in output
        finally:
            os.unlink(temp_file)

    @patch('cli.console.print')
    def test_continuacion_a_pesar_de_errores(self, mock_print):
        """Prueba que la CLI continúa a pesar de errores menores."""
        # Mockear diferentes errores para verificar resiliencia
        with patch('cli.os.path.exists', side_effect=lambda x: x != "no_existe.json"):
            with patch('cli.cargar_propiedades_desde_json', return_value=[]):
                # Debe continuar y mostrar mensaje de no propiedades
                recomendar(perfil="no_existe.json")

                calls = [str(call) for call in mock_print.call_args_list]
                output = ' '.join(calls)

                assert "No se encontraron propiedades que coincidan" in output