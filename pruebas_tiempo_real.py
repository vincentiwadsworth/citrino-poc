#!/usr/bin/env python3
"""
Script para pruebas en tiempo real del sistema de recomendación Citrino
Más rápido y simple que configurar Cherry Studio
"""

import requests
import json
import time
from typing import Dict, Any, List

class PruebasTiempoReal:
    """Clase para realizar pruebas en tiempo real del sistema de recomendación"""

    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.api_recomendar = f"{self.base_url}/api/recomendar"
        self.api_buscar = f"{self.base_url}/api/buscar"
        self.api_estadisticas = f"{self.base_url}/api/estadisticas"

    def verificar_servidor(self) -> bool:
        """Verifica que el servidor esté funcionando"""
        try:
            response = requests.get(f"{self.base_url}/api/health", timeout=5)
            return response.status_code == 200
        except:
            return False

    def probar_recomendacion(self, datos_prospecto: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una prueba de recomendación"""
        try:
            print(f"\n🔄 Probando recomendación para: {datos_prospecto.get('id', 'desconocido')}")

            response = requests.post(
                self.api_recomendar,
                json=datos_prospecto,
                timeout=30
            )

            if response.status_code == 200:
                resultado = response.json()
                if resultado.get('success'):
                    print(f"✅ Éxito: {resultado['total_recomendaciones']} recomendaciones encontradas")
                    return resultado
                else:
                    print(f"❌ Error en la respuesta: {resultado.get('error', 'Error desconocido')}")
                    return {}
            else:
                print(f"❌ Error HTTP: {response.status_code}")
                return {}

        except Exception as e:
            print(f"❌ Error de conexión: {str(e)}")
            return {}

    def mostrar_recomendaciones(self, resultado: Dict[str, Any]) -> None:
        """Muestra las recomendaciones de forma legible"""
        if not resultado or not resultado.get('success'):
            return

        recomendaciones = resultado.get('recomendaciones', [])
        print(f"\n🏠 RECOMENDACIONES ENCONTRADAS ({len(recomendaciones)}):")
        print("-" * 80)

        for i, rec in enumerate(recomendaciones[:5], 1):  # Mostrar solo las 5 primeras
            print(f"{i}. {rec['nombre']}")
            print(f"   💰 Precio: ${rec['precio']:,} USD")
            print(f"   📍 Ubicación: {rec['zona']}")
            print(f"   🏠 Características: {rec['habitaciones']} hab, {rec['banos']} baños, {rec['superficie_m2']} m²")
            print(f"   🎯 Compatibilidad: {rec['compatibilidad']}%")
            print(f"   💡 Justificación: {rec['justificacion']}")
            print()

    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas del sistema"""
        try:
            response = requests.get(self.api_estadisticas, timeout=10)
            if response.status_code == 200:
                return response.json().get('estadisticas', {})
        except:
            pass
        return {}

    def menu_principal(self) -> None:
        """Menú interactivo para pruebas"""
        print("🚀 SISTEMA DE PRUEBAS EN TIEMPO REAL - CITRINO")
        print("=" * 60)

        # Verificar servidor
        if not self.verificar_servidor():
            print("❌ El servidor no está funcionando. Por favor inicia:")
            print("   cd api && python server.py")
            return

        print("✅ Servidor conectado correctamente")

        # Mostrar estadísticas
        stats = self.obtener_estadisticas()
        if stats:
            print(f"📊 Base de datos: {stats.get('total_propiedades', 0):,} propiedades")
            print(f"💰 Precio promedio: ${stats.get('precio_promedio', 0):,.0f} USD")

        while True:
            print("\n" + "=" * 60)
            print("MENÚ DE PRUEBAS:")
            print("1. Probar con perfil de Familia Joven")
            print("2. Probar con perfil de Inversor")
            print("3. Probar con perfil de Profesional Joven")
            print("4. Probar con perfil de Estudiante")
            print("5. Probar con perfil personalizado")
            print("6. Ver estadísticas del sistema")
            print("7. Probar búsqueda simple")
            print("0. Salir")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "0":
                print("👋 ¡Hasta luego!")
                break
            elif opcion == "1":
                self.probar_familia_joven()
            elif opcion == "2":
                self.probar_inversor()
            elif opcion == "3":
                self.probar_profesional_joven()
            elif opcion == "4":
                self.probar_estudiante()
            elif opcion == "5":
                self.probar_personalizado()
            elif opcion == "6":
                self.mostrar_estadisticas_completas()
            elif opcion == "7":
                self.probar_busqueda_simple()
            else:
                print("❌ Opción no válida")

    def probar_familia_joven(self) -> None:
        """Prueba con perfil de familia joven"""
        datos = {
            "id": "familia_joven_test",
            "presupuesto_min": 120000,
            "presupuesto_max": 200000,
            "adultos": 2,
            "ninos": [1],
            "adultos_mayores": 0,
            "zona_preferida": "Equipetrol",
            "tipo_propiedad": "departamento",
            "necesidades": ["seguridad", "estacionamiento", "areas_comunes"]
        }

        resultado = self.probar_recomendacion(datos)
        self.mostrar_recomendaciones(resultado)

    def probar_inversor(self) -> None:
        """Prueba con perfil de inversor"""
        datos = {
            "id": "inversor_test",
            "presupuesto_min": 200000,
            "presupuesto_max": 400000,
            "adultos": 1,
            "ninos": [],
            "adultos_mayores": 0,
            "zona_preferida": "Equipetrol",
            "tipo_propiedad": "departamento",
            "necesidades": ["plusvalia", "rentabilidad", "ubicacion_estrategica"]
        }

        resultado = self.probar_recomendacion(datos)
        self.mostrar_recomendaciones(resultado)

    def probar_profesional_joven(self) -> None:
        """Prueba con perfil de profesional joven"""
        datos = {
            "id": "profesional_joven_test",
            "presupuesto_min": 80000,
            "presupuesto_max": 150000,
            "adultos": 1,
            "ninos": [],
            "adultos_mayores": 0,
            "zona_preferida": "Zona Norte",
            "tipo_propiedad": "departamento",
            "necesidades": ["seguridad", "estacionamiento", "gimnasio"]
        }

        resultado = self.probar_recomendacion(datos)
        self.mostrar_recomendaciones(resultado)

    def probar_estudiante(self) -> None:
        """Prueba con perfil de estudiante"""
        datos = {
            "id": "estudiante_test",
            "presupuesto_min": 30000,
            "presupuesto_max": 80000,
            "adultos": 1,
            "ninos": [],
            "adultos_mayores": 0,
            "zona_preferida": "Centro",
            "tipo_propiedad": "departamento",
            "necesidades": ["precio_accesible", "seguridad", "transporte"]
        }

        resultado = self.probar_recomendacion(datos)
        self.mostrar_recomendaciones(resultado)

    def probar_personalizado(self) -> None:
        """Prueba con perfil personalizado"""
        print("\n🔧 CREAR PERFIL PERSONALIZADO")

        try:
            datos = {
                "id": "personalizado_" + str(int(time.time())),
                "presupuesto_min": int(input("Presupuesto mínimo ($): ") or "0"),
                "presupuesto_max": int(input("Presupuesto máximo ($): ") or "1000000"),
                "adultos": int(input("Número de adultos: ") or "1"),
                "ninos": [],
                "adultos_mayores": int(input("Número de adultos mayores: ") or "0"),
                "zona_preferida": input("Zona preferida: ") or "",
                "tipo_propiedad": input("Tipo de propiedad: ") or "",
                "necesidades": input("Necesidades (separadas por comas): ").split(",")
            }

            # Limpiar necesidades vacías
            datos["necesidades"] = [n.strip() for n in datos["necesidades"] if n.strip()]

            resultado = self.probar_recomendacion(datos)
            self.mostrar_recomendaciones(resultado)

        except ValueError as e:
            print(f"❌ Error en los datos: {e}")

    def probar_busqueda_simple(self) -> None:
        """Prueba búsqueda simple por filtros"""
        print("\n🔍 BÚSQUEDA SIMPLE POR FILTROS")

        try:
            datos = {
                "precio_min": int(input("Precio mínimo ($): ") or "0"),
                "precio_max": int(input("Precio máximo ($): ") or "1000000"),
                "zona": input("Zona (dejar vacío para todas): ") or None,
                "habitaciones_min": int(input("Habitaciones mínimas: ") or "0"),
                "limite": 10
            }

            # Eliminar valores None
            datos = {k: v for k, v in datos.items() if v is not None}

            print("\n🔄 Realizando búsqueda...")
            response = requests.post(self.api_buscar, json=datos, timeout=30)

            if response.status_code == 200:
                resultado = response.json()
                if resultado.get('success'):
                    propiedades = resultado.get('propiedades', [])
                    print(f"✅ Encontradas {len(propiedades)} propiedades")

                    for i, prop in enumerate(propiedades[:5], 1):
                        print(f"\n{i}. {prop['nombre']}")
                        print(f"   💰 ${prop['precio']:,} USD")
                        print(f"   📍 {prop['zona']}")
                        print(f"   🏠 {prop['habitaciones']} hab, {prop['banos']} baños, {prop['superficie_m2']} m²")
                else:
                    print(f"❌ Error: {resultado.get('error', 'Error desconocido')}")
            else:
                print(f"❌ Error HTTP: {response.status_code}")

        except ValueError as e:
            print(f"❌ Error en los datos: {e}")

    def mostrar_estadisticas_completas(self) -> None:
        """Muestra estadísticas completas del sistema"""
        print("\n📊 ESTADÍSTICAS COMPLETAS DEL SISTEMA")
        print("-" * 60)

        stats = self.obtener_estadisticas()

        if stats:
            print(f"Total propiedades: {stats.get('total_propiedades', 0):,}")
            print(f"Precio promedio: ${stats.get('precio_promedio', 0):,.0f}")
            print(f"Precio mínimo: ${stats.get('precio_minimo', 0):,.0f}")
            print(f"Precio máximo: ${stats.get('precio_maximo', 0):,.0f}")
            print(f"Superficie promedio: {stats.get('superficie_promedio', 0):.0f} m²")
            print(f"Total zonas: {stats.get('total_zonas', 0)}")

            print(f"\nTop 10 zonas con más propiedades:")
            zonas = stats.get('distribucion_zonas', {})
            for zona, count in sorted(zonas.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"   • {zona}: {count} propiedades")
        else:
            print("❌ No se pudieron obtener las estadísticas")

def main():
    """Función principal"""
    print("🚀 INICIANDO SISTEMA DE PRUEBAS EN TIEMPO REAL")
    print("Asegúrate de tener el servidor API corriendo:")
    print("   cd api && python server.py")
    print()

    pruebas = PruebasTiempoReal()
    pruebas.menu_principal()

if __name__ == "__main__":
    main()