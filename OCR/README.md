Claro, aquí tienes un archivo `readme.md` que describe el código proporcionado:

```markdown
# Proyecto de Reconocimiento de Texto con EasyOCR

Este proyecto utiliza la biblioteca EasyOCR junto con OpenCV para reconocer texto en una imagen y guardar los resultados en un registro.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas:

- OpenCV (cv2)
- EasyOCR
- pickle

Puedes instalar estas bibliotecas usando `pip`:

```bash
pip install opencv-python-headless easyocr
```

## Uso

1. Asegúrate de tener una imagen que contenga texto en la ruta especificada en la variable `image_path` en el código.
2. Ejecuta el script.

El proceso consta de tres partes principales:

1. **Cargar Resultados Previos:** Si existen resultados previos almacenados en el archivo `resultados.pkl`, se cargarán y mostrarán en la consola.

2. **Procesar la Imagen:** El script cargará la imagen especificada en `image_path` y utilizará EasyOCR para reconocer el texto en la imagen. Los resultados se mostrarán en la consola y se guardarán en el archivo `resultados.pkl`.

3. **Guardar el Registro:** Se guarda un registro de la extracción de texto en el archivo `registro.txt`. El registro incluye información sobre la dirección de la imagen, el texto extraído, la hora de extracción y la confianza promedio en el reconocimiento.

## Archivos

- `main.py`: El código principal que realiza el reconocimiento de texto.
- `diccionario/resultados.pkl`: Un archivo binario donde se guardan los resultados previos.
- `registro/registro.txt`: Un archivo de registro donde se almacenan los detalles de la extracción de texto.
- `images/func.png`: Ejemplo de una imagen de entrada con texto.

## Ejecución

Para ejecutar el proyecto, simplemente ejecuta el archivo `main.py`. Asegúrate de tener una imagen válida en la ruta especificada en `image_path`.

## Resultados

Los resultados de la extracción de texto se mostrarán en la consola y se guardarán en el archivo `registro.txt`. También se almacenarán en `resultados.pkl` para su referencia futura.

¡Disfruta utilizando esta herramienta de reconocimiento de texto con EasyOCR!
```
