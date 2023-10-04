# README.md - Detección de objetos con YOLOv3

Este repositorio contiene un código en Python que utiliza el modelo YOLOv3 para detectar objetos en una imagen. YOLO (You Only Look Once) es un popular modelo de detección de objetos en tiempo real que puede identificar múltiples clases de objetos en una sola pasada. Este README proporciona una visión general del código y cómo utilizarlo.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas antes de ejecutar el código:

- OpenCV (cv2)
- numpy
- requests
- Pillow (PIL)

Puedes instalar estas bibliotecas usando pip:

```
pip install opencv-python numpy requests pillow
```

## Uso

1. **Descargar el modelo YOLOv3 y los archivos de configuración**: Este código espera que los archivos de configuración y pesos del modelo YOLOv3 estén presentes en una carpeta llamada "darknet" en el mismo directorio que el script. Puedes descargar estos archivos desde el sitio web oficial de YOLOv3 o desde otras fuentes confiables.

2. **Descargar el archivo de nombres de clases**: También necesitas un archivo llamado "coco.names" que contenga los nombres de las clases que el modelo puede detectar. Por defecto, el código espera que este archivo esté en la carpeta "darknet". Asegúrate de tenerlo o cámbialo según tus necesidades.

3. **Ejecutar el código**: El código cargará una imagen desde la ubicación especificada en la variable `image_path`. Puedes cambiar esta ubicación para probar diferentes imágenes. Luego, aplicará YOLOv3 para detectar objetos en la imagen y mostrará la imagen resultante con las cajas delimitadoras y etiquetas de clase.

```
python tu_script.py
```

4. **Resultados**: Después de ejecutar el código, se creará una carpeta llamada "results" en la que se guardarán las imágenes con las detecciones. El archivo resultante tendrá el mismo nombre que la imagen de entrada.

## Personalización

Puedes personalizar varios aspectos del código para adaptarlo a tus necesidades:

- Cambiar el umbral de confianza: En la sección de código que filtra las detecciones débiles (`confidence > 0.5`), puedes ajustar el valor de 0.5 a un umbral diferente si deseas ser más o menos restrictivo en las detecciones.

- Cambiar el color y estilo de las cajas delimitadoras y etiquetas de clase: En la sección de código que dibuja las detecciones, puedes modificar los parámetros de `cv2.rectangle` y `cv2.putText` para cambiar el color, grosor de línea, fuente, tamaño de texto, etc.

- Probar con diferentes imágenes: Cambia la variable `image_path` para cargar una imagen diferente y detectar objetos en ella.

## Agradecimientos

Este código utiliza el modelo YOLOv3 y se basa en las bibliotecas OpenCV, numpy, requests y Pillow. Asegúrate de cumplir con las licencias y términos de uso de estas bibliotecas y del modelo YOLOv3 al utilizar este código en tus proyectos.