import cv2

def activarCamara(telefonoNumero):
    echarFoto(telefonoNumero)

def echarFoto(telefono):
    captura = cv2.VideoCapture(0)
    echada = False
    while not echada:
        ok, frame = captura.read()
        cv2.imshow('Cámara', frame)
        cv2.waitKey(10000)

        # Captura la imagen después de los 3 segundos
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

    # Libera los recursos de la cámara
    captura.release()
    cv2.destroyAllWindows()

echarFoto("555")

