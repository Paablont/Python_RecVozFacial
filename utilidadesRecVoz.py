import json
import os


def verificarTelefono(telefono):
    try:
        # Leemos JSON
        with open('Usuarios.json', 'r') as archivo_json:
            data = json.load(archivo_json)

        # Verificamos si existe
        telefonoExiste = any(usuario["telefono"] == telefono for usuario in data["Usuarios"])

        return telefonoExiste
    except json.JSONDecodeError:
        print("Error al decodificar el JSON.")
        return False