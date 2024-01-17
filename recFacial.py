from pathlib import Path
import cv2
import face_recognition as fr


def activarCamara():
    get_photo()

def get_photo():
    captura = cv2.VideoCapture(0)
    #leemos la imagen de la cámara
    while(True):
        ok,frame=captura.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #do some ops
    captura.release()
    cv2.destroyAllWindows()

    if not ok:
        print('No se ha podido recoger la imagen')
    else:
        #Intentaremos reconocer una cara
        cv2.imshow('frame', frame)
        return frame
