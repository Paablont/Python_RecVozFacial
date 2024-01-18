import cv2

def activarCamara(telefonoNumero):
    echarFoto(telefonoNumero)

def echarFoto(telefonoNumero,nombre):
    captura = cv2.VideoCapture(0)
    registrado = False
    print("Preparate, voy a hacer una foto en tres...")
    cv2.waitKey(1000)
    print("dos")
    cv2.waitKey(1000)
    print("uno")
    while not registrado:
        ok, frame = captura.read()
        if ok:
            guardarFoto = f"imagenes/{telefonoNumero}.jpg"
            cv2.imwrite(guardarFoto, frame)
            registrado = True
            print(f"Reconocimiento facial guardado correctamente en la carpeta imagenes")
        else:
            print('No se ha podido recoger la imagen')
            registrado = False
    # do some ops
    captura.release()
    cv2.destroyAllWindows()



