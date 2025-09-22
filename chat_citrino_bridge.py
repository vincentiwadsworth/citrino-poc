#!/usr/bin/env python3
"""
Puente entre Cherry Studio y API Citrino
Permite "chatear con la información" inmobiliaria
"""

import requests
import json
import os
from typing import Dict, Any, List
import openai
from datetime import datetime

class ChatCitrinoBridge:
    """Clase puente para conversaciones con datos inmobiliarios"""

    def __init__(self):
        self.api_url = "http://localhost:5000"
        self.api_recomendar = f"{self.api_url}/api/recomendar"
        self.api_buscar = f"{self.api_url}/api/buscar"
        self.api_estadisticas = f"{self.api_url}/api/estadisticas"

        # Configurar cliente OpenRouter para modelos económicos
        api_key = os.getenv("OPENROUTER_API_KEY", "tu-api-key-openrouter")
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "https://citrino.com",
                "X-Title": "Citrino Chat"
            }
        )

        # Contexto del sistema
        self.system_context = """
Eres un asesor inmobiliario experto de Citrino en Santa Cruz de la Sierra.
Tienes acceso a una base de datos de 76,853 propiedades y 323 proyectos con inteligencia de mercado.
Tu estilo es profesional pero cercano, siempre proporcionando datos concretos y recomendaciones personalizadas.

Cuando recibas una consulta:
1. Analiza la intención del usuario
2. Extrae los parámetros clave (presupuesto, ubicación, tipo de propiedad, necesidades)
3. Realiza la búsqueda en la base de datos
4. Sintetiza los resultados en una respuesta conversacional y útil
5. Proporciona recomendaciones específicas y siguiente pasos

Siempre incluye:
- Saludo profesional
- Análisis de lo que buscan
- Opciones específicas con datos concretos
- Recomendaciones personalizadas
- Siguientes pasos

TUS HERRAMIENTAS DISPONIBLES:
- buscar_propiedades(presupuesto_min, presupuesto_max, zona, tipo_propiedad, habitaciones_min, etc.)
- recomendar_propiedades(perfil_con_necesidades)
- obtener_estadisticas_mercado()
"""

    def consultar_llm(self, messages: List[Dict]) -> str:
        """Consulta al LLM para análisis y síntesis"""
        try:
            response = self.client.chat.completions.create(
                model="qwen/qwen-3-72b-instruct",  # Modelo económico de OpenRouter
                # Alternativas: "google/gemma-2-9b-it", "meta-llama/llama-3.1-8b-instruct"
                messages=messages,
                temperature=0.3,  # Menos temperatura para más consistencia
                max_tokens=800,   # Menos tokens para reducir costos
                top_p=0.9
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error en LLM: {str(e)}"

    def extraer_parametros_busqueda(self, consulta: str) -> Dict[str, Any]:
        """Usa LLM para extraer parámetros de búsqueda del lenguaje natural"""

        prompt = f"""
Extrae los parámetros de búsqueda de esta consulta y conviértelos a JSON:

Consulta: "{consulta}"

Responde SOLO con un JSON válido con estos campos (solo los que se mencionen):
{{
    "presupuesto_min": número,
    "presupuesto_max": número,
    "zona": "texto",
    "tipo_propiedad": "texto",
    "habitaciones_min": número,
    "adultos": número,
    "ninos": [],
    "adultos_mayores": número,
    "necesidades": ["lista"],
    "consulta_tipo": "busqueda|recomendacion|estadisticas"
}}

Ejemplo: {{"presupuesto_min": 150000, "presupuesto_max": 250000, "zona": "Equipetrol", "tipo_propiedad": "departamento"}}
"""

        messages = [
            {"role": "system", "content": "Eres un extractor de parámetros experto. Responde solo con JSON válido."},
            {"role": "user", "content": prompt}
        ]

        try:
            response_json = self.consultar_llm(messages)
            return json.loads(response_json)
        except:
            # Fallback a parámetros básicos
            return {"consulta_tipo": "busqueda"}

    def buscar_propiedades(self, parametros: Dict[str, Any]) -> List[Dict]:
        """Realiza búsqueda de propiedades en la API"""
        try:
            # Limpiar parámetros para la API
            api_params = {}
            for key, value in parametros.items():
                if value is not None and value != "" and value != []:
                    if key in ["presupuesto_min", "presupuesto_max", "habitaciones_min"]:
                        api_params[key] = int(value)
                    elif key == "zona":
                        api_params["zona"] = value
                    elif key == "tipo_propiedad":
                        api_params["tipo_propiedad"] = value

            api_params["limite"] = 10

            response = requests.post(self.api_buscar, json=api_params, timeout=30)
            if response.status_code == 200:
                resultado = response.json()
                if resultado.get('success'):
                    return resultado.get('propiedades', [])
        except Exception as e:
            print(f"Error en búsqueda: {e}")

        return []

    def recomendar_propiedades(self, perfil: Dict[str, Any]) -> List[Dict]:
        """Genera recomendaciones basadas en perfil"""
        try:
            # Formatear perfil para la API
            api_perfil = {
                "id": f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "presupuesto_min": perfil.get("presupuesto_min", 0),
                "presupuesto_max": perfil.get("presupuesto_max", 1000000),
                "adultos": perfil.get("adultos", 1),
                "ninos": perfil.get("ninos", []),
                "adultos_mayores": perfil.get("adultos_mayores", 0),
                "zona_preferida": perfil.get("zona", ""),
                "tipo_propiedad": perfil.get("tipo_propiedad", ""),
                "necesidades": perfil.get("necesidades", [])
            }

            response = requests.post(self.api_recomendar, json=api_perfil, timeout=30)
            if response.status_code == 200:
                resultado = response.json()
                if resultado.get('success'):
                    return resultado.get('recomendaciones', [])
        except Exception as e:
            print(f"Error en recomendación: {e}")

        return []

    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas del mercado"""
        try:
            response = requests.get(self.api_estadisticas, timeout=10)
            if response.status_code == 200:
                resultado = response.json()
                if resultado.get('success'):
                    return resultado.get('estadisticas', {})
        except:
            pass
        return {}

    def sintetizar_respuesta(self, consulta: str, parametros: Dict[str, Any], resultados: List[Dict]) -> str:
        """Usa LLM para sintetizar resultados en respuesta conversacional"""

        # Preparar contexto de resultados
        contexto_resultados = ""
        if resultados:
            for i, prop in enumerate(resultados[:5], 1):
                contexto_resultados += f"""
{i}. {prop.get('nombre', 'Sin nombre')}
   - Precio: ${prop.get('precio', 0):,}
   - Ubicación: {prop.get('zona', 'No especificada')}
   - Características: {prop.get('habitaciones', 0)} hab, {prop.get('banos', 0)} baños, {prop.get('superficie_m2', 0)} m²
   - Garaje: {prop.get('garaje', 'No')}
   - Fuente: {prop.get('fuente', 'No especificada')}
"""
        else:
            contexto_resultados = "No se encontraron propiedades que coincidan con los criterios."

        prompt = f"""
Basado en esta consulta y resultados, genera una respuesta conversacional y profesional:

CONSULTA ORIGINAL: "{consulta}"

PARAMÉTROS EXTRAÍDOS: {json.dumps(parametros, indent=2)}

RESULTADOS ENCONTRADOS:
{contexto_resultados}

REQUISITOS DE RESPUESTA:
1. Saludo profesional y personalizado
2. Reconocimiento de lo que buscan
3. Presentación de las mejores opciones encontradas
4. Análisis y recomendaciones específicas
5. Siguientes pasos sugeridos
6. Cierre con llamada a la acción

Estilo: Asesor inmobiliario experto de Citrino, profesional pero cercano.
Longitud: 2-3 párrafos concisos pero completos.
"""

        messages = [
            {"role": "system", "content": self.system_context},
            {"role": "user", "content": prompt}
        ]

        return self.consultar_llm(messages)

    def procesar_consulta(self, consulta: str) -> str:
        """Procesa una consulta en lenguaje natural y devuelve respuesta"""

        print(f"\n🔄 Procesando consulta: '{consulta}'")

        # 1. Extraer parámetros con LLM
        parametros = self.extraer_parametros_busqueda(consulta)
        print(f"📊 Parámetros extraídos: {parametros}")

        # 2. Determinar tipo de consulta y ejecutar
        consulta_tipo = parametros.get("consulta_tipo", "busqueda")

        if consulta_tipo == "recomendacion":
            # Es una recomendación basada en perfil
            resultados = self.recomendar_propiedades(parametros)
        else:
            # Es una búsqueda directa
            resultados = self.buscar_propiedades(parametros)

        print(f"🏠 Resultados encontrados: {len(resultados)}")

        # 3. Sintetizar respuesta con LLM
        respuesta = self.sintetizar_respuesta(consulta, parametros, resultados)

        return respuesta

    def iniciar_chat_interactivo(self):
        """Inicia chat interactivo para pruebas"""
        print("🏠 CHAT CITRINO - Asesor Inmobiliario Inteligente")
        print("=" * 60)
        print("Escribe tu consulta en lenguaje natural o 'salir' para terminar")
        print("Ejemplos:")
        print("- Busco departamentos en Equipetrol para una familia joven")
        print("- Necesito una casa en Las Palmas con presupuesto de 300k")
        print("- ¿Qué hay disponible para inversión en Zona Norte?")
        print()

        while True:
            consulta = input("👤 Tú: ").strip()

            if consulta.lower() in ['salir', 'exit', 'quit']:
                print("👋 ¡Gracias por usar Chat Citrino!")
                break

            if not consulta:
                continue

            # Procesar consulta
            respuesta = self.procesar_consulta(consulta)

            print(f"\n🤖 Asesor Citrino: {respuesta}")
            print("\n" + "-" * 60)

def main():
    """Función principal"""
    print("🚀 Iniciando Chat Citrino Bridge...")
    print("Asegúrate de tener el servidor API corriendo y la API key de OpenAI configurada")
    print()

    bridge = ChatCitrinoBridge()
    bridge.iniciar_chat_interactivo()

if __name__ == "__main__":
    main()