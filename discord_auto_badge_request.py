# Importamos las bibliotecas necesarias
import discord
import asyncio
import time

# Configuramos los intents para el cliente de Discord
intents = discord.Intents.default()
intents.members = True

# Creamos una instancia del cliente de Discord con los intents configurados
client = discord.Client(intents=intents)

# Decorador para el evento `on_ready`, que se ejecuta cuando el bot se conecta
@client.event
async def on_ready():
    # Imprimimos un mensaje indicando que el bot está conectado
    print('Logged in as {0.user}'.format(client))

    # Establecemos el intervalo de tiempo entre mensajes (20 días en segundos)
    time_interval = 60 * 60 * 24 * 20

    # Bucle infinito para enviar mensajes periódicamente
    while True:
        # Esperamos el tiempo establecido
        await asyncio.sleep(time_interval)
        # Obtenemos el canal donde se enviará el mensaje
        channel = client.get_channel(1064679643426345050)
        # Enviamos el mensaje al canal
        await channel.send('/givemebadge')  # Cambia esto por el mensaje que desees

# Ejecutamos el bot con el token de autenticación
client.run("Aqui_Pones_Tu_Token")


#Correrlo desde la terminal
# & "C:/Users/Alex Gonzalez/AppData/Local/Programs/Python/Python311/python.exe" "c:/Users/Alex Gonzalez/Documents/Codigos_Random/bot_message.py"