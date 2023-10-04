# Proyecto de Chat y Conversión de Texto a Voz

Este proyecto consiste en un script de Python que permite realizar un chat de voz utilizando el servicio de reconocimiento de voz de Google y el modelo de lenguaje de OpenAI, además de convertir las respuestas generadas por OpenAI en voz. A continuación, se proporciona una descripción de las principales funciones y cómo usar el proyecto.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `openai`: Para interactuar con la API de OpenAI.
- `speech_recognition`: Para reconocimiento de voz con Google.
- `google-cloud-texttospeech`: Para la conversión de texto a voz.
- `pydub`: Para la reproducción de archivos de audio.

Asegúrate de configurar correctamente las credenciales de Google Cloud y OpenAI, como se muestra en el código.

## Uso

1. Ejecuta el script `main.py`.
2. El sistema escuchará tu pregunta.
3. Realiza una pregunta en español. El sistema la reconocerá y enviará a OpenAI para obtener una respuesta.
4. La respuesta generada por OpenAI se convertirá en voz.
5. Escucharás la respuesta.

Ten en cuenta que debes tener una conexión a internet activa para que el reconocimiento de voz y la generación de texto a voz funcionen correctamente.

## Configuración de las credenciales

Asegúrate de configurar las siguientes credenciales antes de ejecutar el proyecto:

- `GOOGLE_APPLICATION_CREDENTIALS`: Debe apuntar al archivo JSON de credenciales de Google Cloud.
- `openai.api_key`: Debe contener tu clave de API de OpenAI.

## Personalización

Puedes personalizar la configuración del modelo de lenguaje de OpenAI ajustando los parámetros en la función `generate_text()`. También puedes modificar el idioma de la voz de respuesta en la función `synthesize_speech()`.

## Dependencias

- [OpenAI Python](https://pypi.org/project/openai/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Google Cloud Text-to-Speech](https://pypi.org/project/google-cloud-texttospeech/)
- [Pydub](https://pypi.org/project/pydub/)

¡Disfruta utilizando este proyecto de chat y conversión de texto a voz!
