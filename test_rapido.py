#!/usr/bin/env python3
"""
Script rápido para probar el sistema de recomendación en tiempo real
"""

import requests
import json

# URL del API
URL = "http://localhost:5000/api/recomendar"

# Datos de prueba - Familia joven
datos_prueba = {
    "id": "test_rapido",
    "presupuesto_min": 150000,
    "presupuesto_max": 250000,
    "adultos": 2,
    "ninos": [1],
    "adultos_mayores": 0,
    "zona_preferida": "Equipetrol",
    "tipo_propiedad": "departamento",
    "necesidades": ["seguridad", "estacionamiento", "gimnasio"]
}

print("Probando sistema de recomendacion Citrino...")
print(f"Enviando solicitud a: {URL}")
print(f"Perfil: Familia joven, presupuesto ${datos_prueba['presupuesto_min']:,} - ${datos_prueba['presupuesto_max']:,}")
print()

try:
    response = requests.post(URL, json=datos_prueba, timeout=30)

    if response.status_code == 200:
        resultado = response.json()

        if resultado.get('success'):
            recomendaciones = resultado.get('recomendaciones', [])
            print(f"EXITO: Se encontraron {len(recomendaciones)} recomendaciones")
            print()

            for i, rec in enumerate(recomendaciones[:3], 1):
                print(f"RECOMENDACION {i}:")
                print(f"   Nombre: {rec['nombre']}")
                print(f"   Precio: ${rec['precio']:,} USD")
                print(f"   Ubicacion: {rec['zona']}")
                print(f"   Caracteristicas: {rec['habitaciones']} hab, {rec['banos']} banos, {rec['superficie_m2']} m2")
                print(f"   Compatibilidad: {rec['compatibilidad']}%")
                print(f"   Justificacion: {rec['justificacion']}")
                print()

            print("Sistema funcionando correctamente!")
            print("Usa 'python pruebas_tiempo_real.py' para mas opciones de prueba")

        else:
            print(f"Error en la respuesta: {resultado.get('error', 'Error desconocido')}")

    else:
        print(f"Error HTTP {response.status_code}")
        print("Asegurate de que el servidor este corriendo:")
        print("   cd api && python server.py")

except requests.exceptions.ConnectionError:
    print("Error de conexion")
    print("Asegurate de que el servidor API este iniciado:")
    print("   cd api")
    print("   python server.py")

except Exception as e:
    print(f"Error inesperado: {str(e)}")