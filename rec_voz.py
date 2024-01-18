import json
import os

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


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


def requests():
    reconocido = False
    stop = False
    while not stop:
        # Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'buenos días princesa' in request:
            # reconocido = activarCamara()
            saludo(reconocido)
        if 'quiero registrarme' in request:
            registro()


def registro():
    talk('Di tu nombre')
    nombre = audio_to_text().lower()
    print(nombre)
    while True:
        talk('Proporciona tu número de teléfono')
        telefono = audio_to_text().lower().strip()
        print(telefono)

        try:
            telefonoNumero= int(telefono)
            break
        except ValueError:
            talk('El número de teléfono contiene letras. Por favor, repítelo.')

# Crear un diccionario con la información
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

    talk('Tu información ha sido guardada. Ahora estas dentro de la comunidad')
