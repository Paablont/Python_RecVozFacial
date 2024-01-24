import os
import time
import face_recognition as fr
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

#Este metodo pasa las imagenes de la carpeta "imagenes" a una lista
def imagenesAlista(carpeta):
    #
    path_list = []
    files = os.listdir(carpeta)

    # Filtrar solo los archivos con extensión .jpg
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg'))]

    # Construir la lista de rutas de las imágenes
    for image_file in image_files:
        image_path = os.path.join(carpeta, image_file)
        path_list.append(image_path)

    # La primera será una foto de control, el resto de pruebas
    fotos = [fr.load_image_file(path) for path in path_list]

    return fotos

#La lista de fotos
def asignar_perfil_color(fotos_list):
    for i in range(len(fotos_list)):
        fotos_list[i] = cv2.cvtColor(fotos_list[i], cv2.COLOR_BGR2RGB)
    return fotos_list

def comprobarImagen(imgPath):
    print("Vamos a comprobar")
    img = cv2.imread(imgPath)
    print(img.shape)


echarFoto("777")
listaImagenes = imagenesAlista("imagenes")

listaColor=asignar_perfil_color(listaImagenes)



