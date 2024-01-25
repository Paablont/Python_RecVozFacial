import time

import cv2

def activarCamara(telefonoNumero):
    echarFoto(telefonoNumero)

def echarFoto(telefono):
    captura = cv2.VideoCapture(0)
    echada = False
    start_time = time.time()

    while not echada:
        ok, frame = captura.read()
        cv2.imshow('Cámara', frame)

        # durante 3 segundos
        if time.time() - start_time >= 3:
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
