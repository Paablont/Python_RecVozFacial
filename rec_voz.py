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
    # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.jorge')
    # Pronunciar mensaje
    engine.say(msg)
    engine.runAndWait()


def print_voices():
    engine = pyttsx3.init()
    for voz in engine.getProperty('voices'):
        print(voz.id, voz)

def say_day():
    day = datetime.date.today()
    weekday = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    talk(weekday[day.weekday()])

def say_hour():
    hour = datetime.datetime.now()
    talk(f'En este momento son las {hour.hour} horas y {hour.minute} minutos')


def saludo(reconocido):
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20 and reconocido:
        momento = 'Buenas noches.'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'

    talk(f'{momento} Somos Pablo y Miguel, tus asistentes personales.')

def requests():
    stop = False
    while not stop:
        #Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'Buenos dias princesa' in request:
            print('activar camara')
            #activarCamara()
if __name__ == '__main__':
    requests()