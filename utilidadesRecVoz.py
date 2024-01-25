
import json
import os

from rec_voz import talk, audio_to_text

#Metodo para borrar un usuario del JSON
def borrar(telefono):
    Usuarios = 'Usuarios.json'

    if os.path.exists(Usuarios):
        with open(Usuarios, 'r') as archivoExiste:
            datosExiste = json.load(archivoExiste)
            usuariosCambiar = []

            # Eliminamos por numero de telefono
            for usuario in datosExiste['Usuarios']:
                if usuario['telefono'] != telefono:
                    usuariosCambiar.append(usuario)

            # Actualizamos la lista de usuarios
            datosExiste['Usuarios'] = usuariosCambiar

        with open(Usuarios, 'w') as archivo:
            json.dump(datosExiste, archivo, indent=2)
        talk(f'Usuario con número de teléfono {telefono} eliminado correctamente.')

    else:
        talk('El archivo no existe.')

#Metodo para que al deletrear el numero lo pille con enteros y no con letras
def deletrearNumero():
    talk("Por favor, deletrea el número de teléfono: ")
    deletreo = audio_to_text()
    mapeoNumeros = {
        'cero': '0', 'uno': '1', 'dos': '2', 'tres': '3', 'cuatro': '4',
        'cinco': '5', 'seis': '6', 'siete': '7', 'ocho': '8', 'nueve': '9'
    }

    # Para reemplazar las palabras que decimos por los numeros
    for palabra, numero in mapeoNumeros.items():
        deletreo = deletreo.replace(palabra, numero)

    return deletreo
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