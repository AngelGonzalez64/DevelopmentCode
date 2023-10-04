# Importamos las bibliotecas necesarias
import os
import shutil

def buscar_y_mover_mp3(carpeta_origen, carpeta_destino):
    # Comprobamos si la carpeta de destino existe; si no, la creamos
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Recorremos la estructura de directorios de la carpeta de origen
    for root, dirs, files in os.walk(carpeta_origen):
        # Iteramos sobre cada archivo en la carpeta actual
        for file in files:
            # Comprobamos si el archivo tiene extensión .mp3
            if file.endswith('.mp3'):
                # Construimos las rutas absolutas del archivo de origen y destino
                archivo_origen = os.path.join(root, file)
                archivo_destino = os.path.join(carpeta_destino, file)
                # Movemos el archivo de la carpeta de origen a la de destino
                shutil.move(archivo_origen, archivo_destino)
                # Imprimimos información sobre el archivo movido
                print(f"Archivo {file} movido de {archivo_origen} a {archivo_destino}")

# Rutas a las carpetas de origen y destino
carpeta_principal = 'ruta/a/la/carpeta/principal'
carpeta_destino_mp3 = 'ruta/a/la/carpeta/destino'

# Llamamos a la función buscar_y_mover_mp3 con las rutas especificadas
buscar_y_mover_mp3(carpeta_principal, carpeta_destino_mp3)
