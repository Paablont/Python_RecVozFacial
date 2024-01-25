import os
import time
import cv2
import face_recognition as fr

from utilidadesRecFac import crearCarpetaImagenes, imagenesAlista, borrarImagen


def activarCamara(telefonoNumero):
    echarFoto(telefonoNumero)

def echarFoto(telefono):
    captura = cv2.VideoCapture(0)
    echada = False
    start_time = time.time()


    while not echada:
        ok, frame = captura.read()
        cv2.imshow('Cámara', frame)

        # durante 5 segundos
        if time.time() - start_time >= 5:
            # Captura despues de los 3 segundos
            registrado = False
            while not registrado:
                ok, frame = captura.read()
                if ok:
                    guardarFoto = f"imagenes/{telefono}.jpg"
                    cv2.imwrite(guardarFoto, frame)
                    registrado = True
                    echada = True
                    print(f"Reconocimiento facial guardado correctamente en la carpeta imagenes")
                else:
                    print('No se ha podido recoger la imagen')
                    registrado = False
                    echada = False

        # Checkea
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Liberas los recursos de la camara
    captura.release()
    cv2.destroyAllWindows()

def echarFotoComprobar():
    captura = cv2.VideoCapture(0)
    echada = False
    start_time = time.time()

    while not echada:
        ok, frame = captura.read()
        cv2.imshow('Cámara', frame)

        # durante 5 segundos
        if time.time() - start_time >= 5:
            # Captura despues de los 3 segundos
            registrado = False
            while not registrado:
                ok, frame = captura.read()
                if ok:
                    guardarFoto = f"foto.jpg"
                    cv2.imwrite(guardarFoto, frame)
                    registrado = True
                    echada = True
                else:
                    print('No se ha podido recoger la imagen')
                    registrado = False
                    echada = False

        # Checkea
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Liberas los recursos de la camara
    captura.release()
    cv2.destroyAllWindows()



#La lista de fotos
def asignar_perfil_color(listaImg):
    for i in range(len(listaImg)):
        listaImg[i] = cv2.cvtColor(listaImg[i], cv2.COLOR_BGR2RGB)
    return listaImg


def comprobarImagen(imgPath, listaImg):
    print("Vamos a comprobar")
    img = fr.load_image_file(imgPath)

    # Obtener las características faciales de la imagen
    img_encodings = fr.face_encodings(img)

    #Para comprobar que la foto tenga rasgos humanos
    if not img_encodings:
        print("Lo que aparece en la foto no tiene rasgos humanos")
        return False
    img_encodings = img_encodings[0]

    #Para
    for i, referencia_img in enumerate(listaImg):
            # Obtener las características faciales de la imagen de referencia
            referencia_encodings = fr.face_encodings(referencia_img)[0]
            resultados = fr.compare_faces([referencia_encodings], img_encodings)

    print(f'EN METODOD {resultados}')
    return resultados



