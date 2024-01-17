import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from recFacial import *

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
    # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.jorge')
    # Pronunciar mensaje
    engine.say(msg)
    engine.runAndWait()


def print_voices():
    engine = pyttsx3.init()
    for voz in engine.getProperty('voices'):
        print(voz.id, voz)

def saludo(reconocido):
    hour = datetime.datetime.now()
    if reconocido:
        if hour.hour < 6 or hour.hour > 20:
            momento = 'Buenas noches.'
        elif 6 <= hour.hour < 13:
            momento = 'Buenos días.'
        else:
            momento = 'Buenas tardes.'
        talk(f'{momento} Somos Pablo y Miguel, tus asistentes personales.')
    else:
        talk(f'Somos Pablo y Miguel, tus asistentes personales, no estas registrado en el sistema.'
             f'¿Quieres registrarse?')

def requests():
    reconocido = False
    stop = False
    while not stop:
        #Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'buenos días princesa' in request:
            reconocido = activarCamara()
            saludo(reconocido)
        if 'quiero registrarme' in request:
            talk('Registro en proceso')
