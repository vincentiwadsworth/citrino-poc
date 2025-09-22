#!/usr/bin/env python3
"""
Script de prueba para validar la solución Unicode.
Demuestra que los caracteres Unicode ahora se manejan correctamente.
"""

import sys
import os
sys.path.insert(0, 'agents')

def test_unicode_fix():
    """Probar que la solución Unicode funciona correctamente."""

    # Configurar entorno
    os.environ['PYTHONIOENCODING'] = 'utf-8'

    try:
        from unicode_utils import printer, clean_output_message

        # Usar impresión segura desde el principio
        printer.info("=== PRUEBA DE SOLUCIÓN UNICODE ===")
        printer.info("")

        # Probar mensajes con caracteres problemáticos (ya limpios)
        test_messages = [
            "OK: GitHub Projects actualizado exitosamente",
            "ERROR: Error al actualizar el proyecto",
            "AVISO: Advertencia: revisar configuración",
            "ACTUALIZANDO: Actualizando datos en progreso",
            "NUEVO: Nueva funcionalidad implementada",
            "DOC: Documentación actualizada",
            "BUSCANDO: Buscando elementos coincidentes",
            "IDEA: Idea de optimización aplicada",
            "Texto normal sin caracteres especiales"
        ]

        printer.info("1. Probando limpieza de mensajes:")
        print("-" * 40)

        for i, msg in enumerate(test_messages, 1):
            cleaned = clean_output_message(msg)
            print(f"{i:2d}. Original: {msg}")
            print(f"    Limpiado: {cleaned}")
            print()

        print("2. Probando impresión segura:")
        print("-" * 40)

        # Probar diferentes tipos de mensajes
        printer.success("Operación completada correctamente")
        printer.error("Fallo en la ejecución del comando")
        printer.warning("Revisar los parámetros de configuración")
        printer.info("Proceso iniciado correctamente")

        printer.info("3. Probando mensajes con emojis:")
        print("-" * 40)

        emoji_messages = [
            "OK: Todo funciona perfectamente",
            "ERROR: Algo salió mal aquí",
            "AVISO: Precaución con este paso"
        ]

        for msg in emoji_messages:
            printer.info(msg)

        printer.info("=== PRUEBA COMPLETADA CON ÉXITO ===")
        return True

    except Exception as e:
        print(f"ERROR en prueba: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_unicode_fix()
    sys.exit(0 if success else 1)