#!/usr/bin/env python3
"""
Módulo utilitario para manejo seguro de Unicode en entornos Windows.
Proporciona funciones consistentes para impresión y manejo de caracteres.
"""

import sys
import os
import locale
from typing import Optional

def setup_unicode_environment():
    """Configurar el entorno para manejo seguro de Unicode."""
    # Forzar UTF-8 para salida estándar
    if sys.platform == 'win32':
        os.environ['PYTHONIOENCODING'] = 'utf-8'

        # Configurar locale para manejo de caracteres
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_ALL, '')
            except locale.Error:
                pass  # Usar locale por defecto

def safe_print(message: str, prefix: str = "[PROJECTS_UPDATER]") -> None:
    """Imprimir mensaje de forma segura en cualquier entorno."""
    try:
        full_message = f"{prefix} {message}" if prefix else message
        print(full_message.encode('utf-8', errors='replace').decode('utf-8'))
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Fallback: reemplazar caracteres problemáticos
        safe_message = message.encode('ascii', errors='replace').decode('ascii')
        full_message = f"{prefix} {safe_message}" if prefix else safe_message
        print(full_message)

def remove_problematic_chars(text: str) -> str:
    """Remover caracteres que causan problemas en Windows."""
    problematic_ranges = [
        '\u2700-\u27BF',  # Dingbats
        '\u2600-\u26FF',  # Miscellaneous Symbols
        '\u1F300-\u1F5FF', # Miscellaneous Symbols and Pictographs
        '\u1F600-\u1F64F', # Emoticons
        '\u1F680-\u1F6FF', # Transport and Map Symbols
    ]

    # Reemplazar caracteres problemáticos con texto alternativo
    replacements = {
        'OK:': 'OK:',
        'ERROR:': 'ERROR:',
        'AVISO:': 'AVISO:',
        'ACTUALIZANDO:': 'ACTUALIZANDO:',
        'NUEVO:': 'NUEVO:',
        'DOC:': 'DOC:',
        'BUSCANDO:': 'BUSCANDO:',
        'IDEA:': 'IDEA:',
        'OBJETIVO:': 'OBJETIVO:',
        'ESTRELLA:': 'ESTRELLA:',
        'GRAFICO:': 'GRAFICO:',
        'LANZAR:': 'LANZAR:',
        'CONFIG:': 'CONFIG:',
    }

    result = text
    for char, replacement in replacements.items():
        result = result.replace(char, replacement)

    return result

def clean_output_message(message: str) -> str:
    """Limpiar mensaje de salida para evitar errores Unicode."""
    # Reemplazar caracteres problemáticos
    cleaned = remove_problematic_chars(message)

    # Eliminar caracteres no imprimibles
    cleaned = ''.join(char for char in cleaned if char.isprintable() or char in ['\n', '\r', '\t'])

    return cleaned.strip()

class UnicodeSafePrinter:
    """Clase para manejo seguro de impresión con Unicode."""

    def __init__(self, prefix: str = "[PROJECTS_UPDATER]"):
        self.prefix = prefix
        setup_unicode_environment()

    def print(self, message: str) -> None:
        """Imprimir mensaje de forma segura."""
        cleaned_message = clean_output_message(message)
        safe_print(cleaned_message, self.prefix)

    def success(self, message: str) -> None:
        """Imprimir mensaje de éxito."""
        self.print(f"OK: {message}")

    def error(self, message: str) -> None:
        """Imprimir mensaje de error."""
        self.print(f"ERROR: {message}")

    def warning(self, message: str) -> None:
        """Imprimir mensaje de advertencia."""
        self.print(f"AVISO: {message}")

    def info(self, message: str) -> None:
        """Imprimir mensaje informativo."""
        self.print(f"INFO: {message}")

# Instancia global para uso en los scripts
printer = UnicodeSafePrinter()