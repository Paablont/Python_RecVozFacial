import os
import face_recognition as fr



def crearCarpetaImagenes():
    # Si no existe, la crea
    if not os.path.exists('imagenes'):
        os.makedirs('imagenes')
def borrarImagen():
    os.remove("foto.jpg")

#Este metodo pasa las imagenes de la carpeta "imagenes" a una lista
def imagenesAlista(carpeta):
    #
    path_list = []
    files = os.listdir(carpeta)
    #coge los archivos .jpg,.jpeg POR SI HAY ALGUNA IMAGEN AÑADIDA MAL APOSTA
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg'))]

    # Construir la lista de rutas de las imágenes
    for image_file in image_files:
        image_path = os.path.join(carpeta, image_file)
        path_list.append(image_path)


    fotos = [fr.load_image_file(path) for path in path_list]

    return fotos


