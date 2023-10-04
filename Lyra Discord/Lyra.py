# Para generar un QR
#!generar_qr https://www.ejemplo.com
# @nombre_de_bot generar_qr https://www.ejemplo.com

import discord
from discord.ext import commands
import qrcode
from io import BytesIO
import traceback

#Importaciones locales

# Configuración de las intenciones del bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True 

TOKEN = 'MTA5ODM3MTAyNjUxNTE0NDg0NQ.Ga46v0.V4KzVTIs_9qdyKIbP7GpoahFtMbzPJ6Ds3cwas'
COMMAND_PREFIX = "!"

# Crear el bot con un prefijo de comando y las intenciones configuradas
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), intents=intents)

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name} (ID: {bot.user.id})')
    print('-------------------------------------------------------')

# Comando para generar códigos QR
@bot.command()
async def QR(ctx, *, contenido):
    try:
        if len(contenido) > 500:
            await ctx.send("El contenido debe tener un máximo de 500 caracteres para generar el QR correctamente.")
            return
        
        autor = ctx.author.name
        # Crear un objeto QRCode con el contenido proporcionado
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(contenido)
        qr.make(fit=True)

        # Crear una imagen del código QR en formato BytesIO
        img_io = BytesIO()
        img = qr.make_image(fill_color="white", back_color="#36393F")
        img.save(img_io, "PNG")
        img_io.seek(0)

        # Enviar la imagen del código QR en el canal donde se llamó el comando
        #QR con usuario que lo solicito
        await ctx.send(f'Código QR generado por: {autor}', file=discord.File(img_io, filename="codigo_qr.png"))

        #QR con el contenido del texto
        #await ctx.send(f'Código QR generado para este texo: ||"{contenido}"||', file=discord.File(img_io, filename="codigo_qr.png"))

        # Borrar el mensaje que menciona al bot y el mensaje original que generó el comando
        await ctx.message.delete()
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al generar el código QR: {str(e)}')

# Comando para mostrar estadísticas del servidor
@bot.command()
async def estadisticas(ctx):
    try:
        server = ctx.guild
        member_count = len(server.members)
        role_count = len(server.roles)
        channel_count = len(server.channels)
        text_channels = len(server.text_channels)
        voice_channels = len(server.voice_channels)

        stats_message = f"**Estadísticas del Servidor `{server.name}`:**\n" \
                        f"Miembros: {member_count}\n" \
                        f"Roles: {role_count}\n" \
                        f"Canales: {channel_count}\n" \
                        f"Canales de Texto: {text_channels}\n" \
                        f"Canales de Voz: {voice_channels}"

        await ctx.send(stats_message)
        
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error: {str(e)}')

# Comando para listar los roles del servidor
@bot.command()
async def Roles(ctx):
    server = ctx.guild
    roles_info = []

    for role in server.roles:
        #Nombre, id de roles
        #roles_info.append(f"Nombre: {role.name}, ID: {role.id}")
        
        #Nombre de roles
        roles_info.append(f"Nombre: {role.name}")

    roles_list_message = "\n".join(roles_info)
    await ctx.send(f"Roles en el servidor:\n{roles_list_message}")

# Comando para asignar un rol a un miembro
@bot.command()
async def asignar_rol(ctx, rol: discord.Role, miembro: discord.Member):
    try:
        await miembro.add_roles(rol)
        await ctx.send(f'Se asignó el rol **{rol.name}** a {miembro.display_name}.')
    except discord.Forbidden:
        await ctx.send("No tengo permisos para asignar roles o el rol que intentas asignar es superior al mío.")
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error: {str(e)}')

# Comando para quitar un rol a un miembro
@bot.command()
async def quitar_rol(ctx, rol: discord.Role, miembro: discord.Member):
    try:
        await miembro.remove_roles(rol)
        await ctx.send(f'Se quitó el rol **{rol.name}** a {miembro.display_name}.')
    except discord.Forbidden:
        await ctx.send("No tengo permisos para quitar roles o el rol que intentas quitar es superior al mío.")
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error: {str(e)}')

# Iniciar el bot con el token
try:
    bot.run(TOKEN)
except Exception as e:
    print(f'Error al iniciar el bot: {e}')
