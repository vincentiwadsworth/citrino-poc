# Configuración de Variables de Entorno - Chat Citrino

## Configuración Requerida

### 1. OpenRouter API Key
Regístrate en [OpenRouter.ai](https://openrouter.ai) y obtén una API key.

Modelos recomendados por costo/eficiencia:
- `qwen/qwen-3-72b-instruct` - $0.50/M tokens (recomendado)
- `google/gemma-2-9b-it` - $0.20/M tokens
- `meta-llama/llama-3.1-8b-instruct` - $0.18/M tokens
- `glm/glm-4-air` - $0.10/M tokens

### 2. Configuración del Archivo .env
Crea un archivo `.env` en la raíz del proyecto:

```bash
# OpenRouter API Key
OPENROUTER_API_KEY=sk-or-tu-api-key-aqui

# Modelo (opcional, usa qwen-3-72b por defecto)
OPENROUTER_MODEL=qwen/qwen-3-72b-instruct

# API Citrino (local)
CITRINO_API_URL=http://localhost:5000
```

## Estimación de Costos

### Cálculo por consulta:
- Extracción de parámetros: ~500 tokens ($0.00025)
- Síntesis de respuesta: ~800 tokens ($0.00040)
- Total por consulta: ~1300 tokens ($0.00065)

### Costo mensual (estimado):
- 100 consultas/día: $19.50/mes
- 500 consultas/día: $97.50/mes
- 1000 consultas/día: $195.00/mes

## Alternativas

### Opción 1: Modelo Nativo de Cherry Studio
Si Cherry Studio tiene capacidades de function calling, podría consumir directamente la API Citrino sin necesidad del bridge.

### Opción 2: Modelo Local
Instalar Ollama y usar modelos locales:
```python
# Configuración para Ollama (local, gratis)
self.client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
# Usar modelo: "llama3.1:8b", "qwen2.5:7b"
```

## Pruebas sin Costos

Para probar sin incurrir en costos:

1. **Modo simulación**: Comenta las llamadas reales al LLM y usa respuestas mock
2. **Modelos gratuitos**: Algunos modelos tienen tiers gratuitos limitados
3. **Pruebas locales**: Usa Ollama con modelos descargados localmente

## Configuración Cherry Studio

### Para integrar con Cherry Studio:

1. Iniciar el bridge:
```bash
python chat_citrino_bridge.py
```

2. Configurar Cherry Studio:
- Base URL: `http://localhost:8000`
- Model: `citrino-chat`
- API Key: la misma de OpenRouter

3. Probar con consultas en lenguaje natural

## Monitoreo de Costos

OpenRouter proporciona dashboard para monitorear:
- Uso por modelo
- Costos acumulados
- Límites de consumo

Revisar periódicamente para optimizar selección de modelos según rendimiento vs costo.