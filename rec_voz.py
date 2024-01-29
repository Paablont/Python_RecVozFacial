import json
import os
import sys
from pathlib import *
import pyttsx3
import speech_recognition as sr
import datetime
from recFacial import *
from utilidadesRecFac import borrarImagenUsuario
from utilidadesRecVoz import  verificarTelefono


#Metodo para que reconozca la voz y la pase a texto
def audio_to_text():
    # Recognizer
    r = sr.Recognizer()

    # Configurar el micro
    with sr.Microphone() as origen:
        # Tiempo de espera desde que se activa el micro
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print('Puedes comenzar a hablar')

        # Guardar audio
        audio = r.listen(origen)

        try:
            # Buscar en google lo escuchado
            text = r.recognize_google(audio, language='es-es')
            print(text)
            return text
        except sr.UnknownValueError:
            print('Ups, no entendí lo que dijiste')
            return 'Esperando'

        except sr.RequestError:
            print('Ups, sin servicio')
            return 'Esperando'

        except:
            print('Ups, algo ha salido mal')
            return 'Esperando'

#Metodo para que la maquina lea en voz alta los mensajes
def talk(msg):
    # Encender el motor pyttsx3
    engine = pyttsx3.init()
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.jorge')
    # Pronunciar mensaje
    engine.say(msg)
    engine.runAndWait()


def print_voices():
    engine = pyttsx3.init()
    for voz in engine.getProperty('voices'):
        print(voz.id, voz)

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
                    borrarImagenUsuario(telefono)
                    talk(f'Usuario con número de teléfono {telefono} eliminado correctamente.')
                    # Actualizamos la lista de usuarios
                    datosExiste['Usuarios'] = usuariosCambiar


        with open(Usuarios, 'w') as archivo:
            json.dump(datosExiste, archivo, indent=2)


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

def saludo(reconocido):
    print(f"FUNCION {reconocido}")
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        momento = 'Buenas noches.'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'
    if reconocido:
        talk(f'{momento} ya estas registrado en el sistema. Bienvenido de nuevo')
        talk('Puedes hacer varias opciones: '
             'Para borrar el usuario di: Borrar usuario. '
             'Para cerrar la sesion actual di: Cerrar sesion. '
             'Para salir del programa di: Salir del programa')
    else:
        talk(f'{momento} no estas registrado en el sistema.')
        talk(f' ¿Quiere registrarse?. Para registrarse, diga: Quiero registrarme')

#Metodo para salir del programa
def salir():
    borrarImagen()
    sys.exit()

#Metodo para registrar nuevo usuario (Comprueba si el numero de telef ya existe o no)
def registro():
    Usuarios = 'Usuarios.json'
    talk('Di tu nombre')
    nombre = audio_to_text().lower()
    print(nombre)

    while True:
        # Quitamos los espacios de todos lados por si da error
        telefono = deletrearNumero().replace(' ', '').split()
        print(telefono)
        try:
            # Para pasar de String [] a un int
            telefonoNumero = int(''.join(telefono))
            if os.path.exists(Usuarios):
                if verificarTelefono(telefonoNumero):
                    talk('El número de teléfono ya está registrado. Por favor, elige otro.')
                    print(verificarTelefono(telefonoNumero))
                else:
                    break
            else:
                break
        except ValueError:
            talk('El número de teléfono contiene letras. Por favor, repítelo.')
    talk("Preparate, vamos a guardar una foto tuya")
    echarFoto(telefonoNumero)

# Crear un diccionario con la información para añadirlo a un fichero JSON
    usuario = {
        'nombre': nombre,
        'telefono': telefonoNumero
    }

    if os.path.exists(Usuarios):
        with open(Usuarios, 'r') as archivoExiste:
            datosExiste = json.load(archivoExiste)

        datosExiste['Usuarios'].append(usuario)

        with open(Usuarios, 'w') as archivo:
            json.dump(datosExiste, archivo, indent=2)
    else:
        with open(Usuarios, 'w') as archivo:
            json.dump({'Usuarios': [usuario]}, archivo, indent=2)

    talk(f'Tu información ha sido guardada. .Bienvenido {nombre}')
    talk('Puedes hacer varias opciones: '
         'Para borrar el usuario di: Borrar usuario. '
         'Para cerrar la sesion actual di: Cerrar sesion. '
         'Para salir del programa di: Salir del programa')

#Metodo para ejecutar el programa entero
def cerrarSesion():
    requests()

def requests():
    crearCarpetaImagenes()
    reconocido = False
    stop = False
    #talk("Iniciando el sistema de reconocimiento a la clase de DAM. "
      #   "Vamos a proceder a realizar un reconocimiento facial")
    #talk("Para iniciar el sistema di: buenos dias princesa. Para salir: salir del programa")
    while not stop:
        # Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'buenos días princesa' in request:

            echarFotoComprobar()
            listaImagenes = imagenesAlista("imagenes")
            if len(listaImagenes) != 0:
                listaColor = asignar_perfil_color(listaImagenes)
                reconocido = comprobarImagen("temp.jpg", listaColor)
                print(f"MAIN {reconocido}")
            saludo(reconocido)

        if 'quiero registrarme' in request:
            registro()
        if 'salir del programa' in request:
            borrarImagen()
            salir()
        if 'borrar usuario' in request:
            while True:
                # Quitamos los espacios de todos lados por si da error
                telefono = deletrearNumero().replace(' ', '').split()
                print(telefono)
                try:
                    # Para pasar de String [] a un int
                    telefonoNumero = int(''.join(telefono))
                    #telefonoNumero = int(''.join(telefono))
                    borrar(telefonoNumero)
                    break
                except ValueError:
                    talk('El número de teléfono contiene letras. Por favor, repítelo.')

        if 'cerrar sesión' in request:
            borrarImagen()
            talk('Se ha cerrado la sesion. Reiniciando el sistema... ')
            cerrarSesion()
