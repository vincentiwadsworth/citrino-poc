#!/usr/bin/env python3
"""
Agente especializado para actualizar GitHub Projects automáticamente después de commits.
Este agente se integra con el flujo de trabajo de Claude Code.
"""

import subprocess
import json
import re
import os
from datetime import datetime
from unicode_utils import printer

def run_command(cmd):
    """Ejecutar un comando y retornar la salida."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        printer.error(f"Error ejecutando comando: {e}")
        return None

def get_latest_commit_message():
    """Obtener el mensaje del último commit."""
    return run_command("git log -1 --pretty=format:'%s'")

def get_latest_commit_hash():
    """Obtener el hash del último commit."""
    return run_command("git log -1 --pretty=format:'%h'")

def update_project_status(commit_message, commit_hash):
    """Actualizar el estado de las tarjetas del proyecto basado en el commit."""

    # Configuración del proyecto
    project_id = "PVT_kwHOCLQG084BDlEf"
    status_field_id = "PVTSSF_lAHOCLQG084BDlEfzg1dQvI"
    done_option_id = "98236657"
    in_progress_option_id = "47fc9ee4"  # ID para "In Progress"

    # Mapeo de palabras clave a IDs de items
    item_mapping = {
        'commit 1': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'commit 2': 'PVTI_lAHOCLQG084BDlEfzge9tOc',
        'commit 3': 'PVTI_lAHOCLQG084BDlEfzge9tOk',
        'commit 4': 'PVTI_lAHOCLQG084BDlEfzge9tOs',
        'commit 5': 'PVTI_lAHOCLQG084BDlEfzge9tO4',
        'estructura': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'motor': 'PVTI_lAHOCLQG084BDlEfzge9tOc',
        'test': 'PVTI_lAHOCLQG084BDlEfzge9tOk',
        'cli': 'PVTI_lAHOCLQG084BDlEfzge9tOs',
        'optimizacion': 'PVTI_lAHOCLQG084BDlEfzge9tO4',
        'docs': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'readme': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'limpiar': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'mejorar': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'actualizar': 'PVTI_lAHOCLQG084BDlEfzge9tNs',
        'feat': 'PVTI_lAHOCLQG084BDlEfzge9tOc',
        'fix': 'PVTI_lAHOCLQG084BDlEfzge9tOc',
        'refactor': 'PVTI_lAHOCLQG084BDlEfzge9tO4',
        'chore': 'PVTI_lAHOCLQG084BDlEfzge9tO4'
    }

    # Analizar el commit para determinar qué tarjeta actualizar
    commit_lower = commit_message.lower()
    commit_hash_short = commit_hash[:7]

    printer.info(f"Analizando commit: {commit_hash_short} - {commit_message}")

    # Buscar el item correspondiente
    item_to_update = None
    for keyword, item_id in item_mapping.items():
        if keyword in commit_lower:
            item_to_update = item_id
            printer.info(f"Item encontrado: {item_id} (keyword: {keyword})")
            break

    if item_to_update:
        # Actualizar el status del item a "Done"
        cmd = f'gh project item-edit --id {item_to_update} --field-id {status_field_id} --single-select-option-id {done_option_id} --project-id {project_id}'
        printer.info(f"Ejecutando: {cmd}")
        result = run_command(cmd)

        if result is not None:
            printer.success(f"Item {item_to_update} actualizado a 'Done'")
            return True
        else:
            printer.error(f"No se pudo actualizar el item {item_to_update}")
            return False
    else:
        printer.warning("No se encontró un item correspondiente al commit message")
        return False

def create_new_item_if_needed(commit_message, commit_hash):
    """Crear un nuevo item si el commit no coincide con existentes."""
    # Extraer tipo de commit y mensaje limpio
    commit_match = re.match(r'^(docs|feat|fix|test|perf|refactor|chore|build|style):\s*(.+)', commit_message)

    if commit_match:
        commit_type, clean_message = commit_match.groups()
        item_title = f"{commit_type}: {clean_message}"

        project_id = "PVT_kwHOCLQG084BDlEf"

        # Crear nuevo item
        cmd = f'gh project item-create --project-id {project_id} --title "{item_title}" --body "Commit: {commit_hash}"'
        printer.info(f"Creando nuevo item: {cmd}")

        result = run_command(cmd)
        if result:
            printer.success(f"Nuevo item creado: {item_title}")
            return True
        else:
            printer.error("No se pudo crear el item")
            return False

    return False

def main():
    """Función principal del agente."""
    printer.info("Iniciando actualización de GitHub Projects...")

    # Obtener información del último commit
    commit_message = get_latest_commit_message()
    commit_hash = get_latest_commit_hash()

    if not commit_message:
        printer.error("No se pudo obtener el último commit")
        return False

    printer.info(f"Último commit: {commit_hash} - {commit_message}")

    # Intentar actualizar un item existente
    success = update_project_status(commit_message, commit_hash)

    # Si no se encontró item, crear uno nuevo
    if not success:
        printer.info("Intentando crear nuevo item...")
        success = create_new_item_if_needed(commit_message, commit_hash)

    if success:
        printer.success("GitHub Projects actualizado exitosamente")
        return True
    else:
        printer.error("No se pudo actualizar GitHub Projects")
        return False

if __name__ == "__main__":
    main()