import discord
from discord.ext import commands

# *********************************
# **    Importaciones Locales    **
# *********************************
from config import TOKEN, COMMAND_PREFIX
from presences import *
from Commands.Roles import *
from Commands.Entertainment import *
from Commands.Information import *
from Commands.Security import *
from Commands.Call import *

# ****************************************************
# **    Configuración de las Intenciones del Bot    **
# ****************************************************
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

# Crear el bot con un prefijo de comando y las intenciones configuradas
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), intents=intents)

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    
    print(f'Bot conectada como {bot.user.name} (ID: {bot.user.id})')
    print('-------------------------------------------------------')

    # Enviar un mensaje al canal general cuando el bot se conecta
    await saludo_principal(bot)
    # Configurar la presencia del las actividades del bot
    await set_bot_presence(bot)

# Llamada de Comandos
Code_QR(bot)
Server_Info(bot)
Mostrar_Roles(bot)
Crear_Rol(bot)
Asignar_Rol(bot)
Quitar_Rol(bot)
Eliminar_Rol(bot)
User_Info(bot)
Lyra_Info(bot)
Moneda(bot)
Password(bot)
Ruleta_Rusa(bot)
Anonimo(bot)
Code_Morse(bot)
Latencia(bot)
Estadisticas_Bot_Info(bot)
Ayuda(bot)
Join_Llamada(bot)
Exit_Call(bot)

# COMANDOS
#//=============================================//

# Security
#@Lyra QR <contenido>
#@Lyra password <int>
#@Lyra mensaje_anonimo <#canal> <contenido>
#@Lyra morse <contenido>

# Roles
#@Lyra roles
#@Lyra crear_rol <contenido>
#@Lyra asignar_rol <@rol> <@miembro>
#@Lyra quitar_rol <@rol> <@miembro>
#@Lyra eliminar_rol <@rol>

# Information
#@Lyra Lyra
#@Lyra userinfo <@miembro>
#@Lyra stats
#@Lyra estadisticas
#@Lyra ayuda <Comando>
#@Lyra ping

# Entertainment
#@Lyra moneda
#@Lyra ruleta

# Call
#@Lyra unirse
#@Lyra salir


# Iniciar el bot con el token
try:
    bot.run(TOKEN)
except Exception as e:
    print(f'Error al iniciar el bot: {e}')
