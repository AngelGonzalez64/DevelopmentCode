import cv2
import easyocr
import pickle
from datetime import datetime

# Rutas de archivos
result_file = 'diccionario/resultados.pkl'
registro_file = 'registro/registro.txt'
image_path = 'images/func.png'

def cargar_resultados():
    try:
        with open(result_file, 'rb') as file:
            saved_results = pickle.load(file)
        print("Resultados previos cargados:")
        for result in saved_results:
            print(result)
        print()
    except FileNotFoundError:
        saved_results = []
    return saved_results

def guardar_resultados(results):
    with open(result_file, 'wb') as file:
        pickle.dump(results, file)

def guardar_registro(results, average_confidence_percentage):
    try:
        with open(registro_file, 'a', encoding='utf-8') as file:
            file.write("Dirección de imagen: {}\n".format(image_path))
            file.write("Texto extraído:\n")
            for res in results:
                lines = res[1].split('\n')
                for line in lines:
                    file.write("{}\n".format(line))
                file.write("----\n")
            file.write("Hora de extracción: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            file.write("Confianza promedio: {:.2f}%\n".format(average_confidence_percentage))
            file.write("■-----------------------------------------------------------------------------■\n")
        print("Registro guardado con éxito.")
    except Exception as e:
        print("Error al guardar el registro: {}".format(str(e)))


def procesar_imagen(image_path):
    image = cv2.imread(image_path)
    reader = easyocr.Reader(['es'])
    result = reader.readtext(image)

    print("Texto reconocido:")
    for res in result:
        text = res[1]
        confidence = res[2]
        print(text)
        saved_results.append(text)

    guardar_resultados(saved_results)

    confidence_list = [res[2] for res in result]
    average_confidence = sum(confidence_list) / len(confidence_list)
    average_confidence_percentage = average_confidence * 100

    guardar_registro(result, average_confidence_percentage)

# Cargar resultados guardados, si existen
saved_results = cargar_resultados()

# Procesar la imagen
procesar_imagen(image_path)
