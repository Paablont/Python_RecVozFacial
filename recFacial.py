import cv2


def echarFoto(telefonoNumero):
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
            print("Usuario registrado correctamente")
        else:
            print('No se ha podido recoger la imagen')
            registrado = False
    # do some ops
    captura.release()
    cv2.destroyAllWindows()



