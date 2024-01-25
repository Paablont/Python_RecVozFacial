import json
import os
import sys
from pathlib import *
import pyttsx3
import speech_recognition as sr
import datetime
from recFacial import *
from utilidadesRecVoz import deletrearNumero, borrar, verificarTelefono


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


def saludo(reconocido):
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        momento = 'Buenas noches.'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'
    if reconocido:
        talk(f'{momento} Somos Pablo y Miguel, tus asistentes personales.')
    else:
        talk(f'{momento} Somos Pablo y Miguel, tus asistentes personales, no estas registrado en el sistema.')
        talk(f' ¿Quiere registrarse?. Para registrarse, diga: Quiero registrarme')

#Metodo para salir del programa
def salir():
    sys.exit()



#Metodo para registrar nuevo usuario (Comprueba si el numero de telef ya existe o no)
def registro():
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
            if verificarTelefono(telefonoNumero):
                talk('El número de teléfono ya está registrado. Por favor, elige otro.')
                print(verificarTelefono(telefonoNumero))
            else:
                break
        except ValueError:
            talk('El número de teléfono contiene letras. Por favor, repítelo.')
    echarFoto(telefonoNumero)

# Crear un diccionario con la información para añadirlo a un fichero JSON
    usuario = {
        'nombre': nombre,
        'telefono': telefonoNumero
    }

    Usuarios = 'Usuarios.json'
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

#Metodo para comprobar si el telefono existe o no en el JSON


#Metodo para ejecutar el programa entero
def requests():
    reconocido = False
    stop = False
    while not stop:
        # Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'buenos días princesa' in request:
            #reconocido = activarCamara()
            saludo(reconocido)
        if 'quiero registrarme' in request:
            registro()
        if 'salir del programa' in request:
            salir()
        if 'borrar usuario' in request:
            borrar()