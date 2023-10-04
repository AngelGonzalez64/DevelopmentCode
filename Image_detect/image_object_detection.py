from pydoc import classname
import cv2
import os
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# Definir la función para cargar la imagen desde una URL o ruta local
def load_image(path):
    if path.startswith('http'):
        response = requests.get(path)
        image = Image.open(BytesIO(response.content))
    else:
        image = Image.open(path)
    return image

# Cargar las clases disponibles
with open("darknet/coco.names", "r") as f:
    classes = f.read().splitlines()

# Cargar el modelo YOLOv3
net = cv2.dnn.readNetFromDarknet("darknet/yolov3.cfg", "darknet/yolov3.weights")

# Obtener las capas de salida
output_layers = net.getUnconnectedOutLayersNames()

# Cargar la imagen de entrada
image_path = "image/ocean.jpg"
image = load_image(image_path)

# Obtener las dimensiones de la imagen
width, height = image.size

# Preprocesar la imagen para la entrada en el modelo
blob = cv2.dnn.blobFromImage(np.array(image), 1/255.0, (416, 416), swapRB=True, crop=False)

# Establecer la entrada al modelo
net.setInput(blob)

# Obtener las salidas de todas las capas de salida
outputs = net.forward(output_layers)

# Inicializar listas para las cajas delimitadoras, confianzas y clases
boxes = []
confidences = []
class_ids = []

# Iterar sobre cada una de las salidas
for output in outputs:
    # Iterar sobre cada detección
    for detection in output:
        # Obtener las probabilidades de las clases y las confianzas
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # Filtrar detecciones débiles por confianza
        if confidence > 0.5:
            # Escalar las coordenadas de la caja delimitadora al tamaño original de la imagen
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Calcular las coordenadas de la esquina superior izquierda de la caja delimitadora
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # Agregar las coordenadas, confianzas y clases a las listas correspondientes
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Aplicar supresión no máxima para eliminar detecciones superpuestas
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Verificar si se encontraron objetos en la imagen
if len(indexes) > 0:
    # Crear la carpeta de resultados si no existe
    os.makedirs("results", exist_ok=True)

# Convertir la imagen a una matriz NumPy
image_np = np.array(image)

# Dibujar las detecciones en la imagen
for i in indexes.flatten():
    # Obtener las coordenadas y dimensiones de la caja delimitadora
    x, y, w, h = boxes[i]

    # Dibujar la caja delimitadora y el texto de la clase y confianza
    cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(image_np, f"{classname}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Convertir la matriz NumPy de vuelta a la imagen PIL
image_with_detections = Image.fromarray(image_np)

# Guardar la imagen con las detecciones en la carpeta de resultados
image_with_detections.save(f"results/{image_path.split('/')[-1]}")

# Mostrar la imagen con las detecciones
image_with_detections.show()
