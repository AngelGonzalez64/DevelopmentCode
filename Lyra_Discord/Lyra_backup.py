#Optimiza: para que tenga un mejor rendimiento
#Limpia: quita todo loq no se ocupe o sea inecesario
#Comenta: Añade comentarios al codigo y para cada comando
#Organiza: Acomoda todos los comandos, importaciones etc
#Relleno: Añade mas contenido a cada comando 
#Comando: Crear un rol


import datetime
import discord
from discord.ext import commands, tasks
import qrcode
from io import BytesIO
import traceback
import random
import string
import secrets

# Importaciones locales
from config import TOKEN, COMMAND_PREFIX
from help import commands_list
from color_embed import color_Embed

# Configuración de las intenciones del bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True

# Crear el bot con un prefijo de comando y las intenciones configuradas
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), intents=intents)

start_time = datetime.datetime.now()

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name} (ID: {bot.user.id})')
    print('-------------------------------------------------------')


    # Define la presencia del bot de manera personalizada
    custom_presence = discord.Activity(
        type=discord.ActivityType.playing,
        name="Conquistar Alemania 🚀",
        details="¡Dominando el mundo!",
        state=f"En {len(bot.guilds)} servidores"
    )

    await bot.change_presence(
        activity=custom_presence,
        status=discord.Status.online
    )


# Comando para generar códigos QR
@bot.command()
async def QR(ctx, *, contenido):
    try:
        if len(contenido) > 500:
            await ctx.send("El contenido debe tener un máximo de 500 caracteres para generar el QR correctamente.")
            return

        autor = ctx.author.name

        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["QR"]
        color = discord.Colour.from_rgb(*color_tuple)

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

        # Crear un Embed para la respuesta
        embed = discord.Embed(title="Codigo QR generado", color=color)
        embed.set_author(name=f"Solicitado por: {autor}", icon_url=ctx.author.avatar.url)
        embed.set_image(url="attachment://codigo_qr.png")

        # Envia el Embed con la imagen del código QR en el canal donde se llamó el comando
        await ctx.send(embed=embed, file=discord.File(img_io, filename="codigo_qr.png"))

        # Borrar el mensaje que menciona al bot y el mensaje original que generó el comando
        await ctx.message.delete()
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al generar el código QR: {str(e)}')

# Comando para mostrar estadísticas del servidor
@bot.command()
async def estadisticas(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["estadisticas"]
        color = discord.Colour.from_rgb(*color_tuple)

        server = ctx.guild
        member_count = len(server.members)
        role_count = len(server.roles)
        channel_count = len(server.channels)
        text_channels = len(server.text_channels)
        voice_channels = len(server.voice_channels)
        category_count = len(server.categories)
        emoji_count = len(server.emojis)
        online_members = sum(1 for member in server.members if member.status != discord.Status.offline)
        offline_members = sum(1 for member in server.members if member.status != discord.Status.online)

        embed = discord.Embed(title=f"Estadísticas del Servidor {server.name}", color=color)
        embed.set_thumbnail(url=server.icon.url)
        embed.add_field(name="Miembros Totales", value=member_count)
        embed.add_field(name="No. Roles", value=role_count)
        embed.add_field(name="Canales Totales", value=channel_count)
        embed.add_field(name="Canales de Texto", value=text_channels)
        embed.add_field(name="Canales de Voz", value=voice_channels)
        embed.add_field(name="Categorías", value=category_count)
        embed.add_field(name="Emojis", value=emoji_count)
        embed.add_field(name="Miembros en Línea", value=online_members)
        embed.add_field(name="Miembros Desconectados", value=offline_members)

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al dar las Estadísticas: {str(e)}')

@bot.command()
async def roles(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["roles"]  # Valor por defecto si no se encuentra
        color = discord.Colour.from_rgb(*color_tuple)

        server = ctx.guild

        # Obtener información detallada de los roles
        roles_info = []
        for role in sorted(server.roles, key=lambda role: role.position, reverse=True):
            if role.name != "@everyone":
                role_info = f"{role.mention} ({len(role.members)} miembros)"
                roles_info.append(role_info)

        roles_list_message = "\n".join(roles_info)

        # Crear un Embed para la lista de roles
        embed = discord.Embed(
            title=f"Roles en el Servidor ({len(server.roles) - 1} roles)",  # Restar 1 para excluir "@everyone"
            description=roles_list_message,
            color=color
        )
        embed.set_thumbnail(url=server.icon.url)
        embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar.url)

        # Enviar el Embed en el canal donde se llamó el comando
        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al mostrar los Roles: {str(e)}')


# Comando para asignar un rol a un miembro
@bot.command()
async def asignar_rol(ctx, rol: discord.Role, miembro: discord.Member):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["asignar_rol"]
        color = discord.Colour.from_rgb(*color_tuple)

        await miembro.add_roles(rol)

        # Crear un Embed informativo
        embed = discord.Embed(title="Asignación de Rol", color=color)
        embed.add_field(name="Rol asignado", value=rol.mention, inline=False)
        embed.add_field(name="Miembro", value=miembro.mention, inline=False)
        embed.set_footer(text=f"Asignado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=miembro.avatar.url)

        await ctx.send(embed=embed)

    except discord.Forbidden:
        await ctx.send("No tengo permisos para asignar roles o el rol que intentas asignar es superior al mío.")
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al asignar un rol: {str(e)}')

# Comando para quitar un rol a un miembro
@bot.command()
async def quitar_rol(ctx, rol: discord.Role, miembro: discord.Member):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["quitar_rol"]
        color = discord.Colour.from_rgb(*color_tuple)

        await miembro.remove_roles(rol)

        # Crear un Embed informativo
        embed = discord.Embed(title="Quitar Rol", color=color)
        embed.add_field(name="Rol retirado", value=rol.mention, inline=False)
        embed.add_field(name="Miembro", value=miembro.mention, inline=False)
        embed.set_footer(text=f"Retirado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=miembro.avatar.url)

        await ctx.send(embed=embed)

    except discord.Forbidden:
        await ctx.send("No tengo permisos para quitar roles o el rol que intentas quitar es superior al mío.")
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al quitar un rol: {str(e)}')

# Comando para solicitar la información de un usuario
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["userinfo"]
        color = discord.Colour.from_rgb(*color_tuple)

        if member is None:
            member = ctx.author

        embed = discord.Embed(title=f"Información de {member.name}", color=color)
        embed.set_thumbnail(url=member.avatar.url)

        # Información básica
        embed.add_field(name="Nombre de usuario", value=member.name, inline=True)
        embed.add_field(name="Apodo", value=member.nick if member.nick else "N/A", inline=True)
        embed.add_field(name="ID de usuario", value=member.id, inline=False)
        embed.add_field(name="Cuenta creada el", value=member.created_at.strftime("%d de %B de %Y a las %H:%M:%S"), inline=False)
        embed.add_field(name="Se unió al servidor el", value=member.joined_at.strftime("%d de %B de %Y a las %H:%M:%S"), inline=False)

        # Roles del usuario
        roles_str = ", ".join([role.mention for role in member.roles[1:]])
        embed.add_field(name="Roles", value=roles_str if roles_str else "N/A", inline=False)

        await ctx.send(embed=embed)
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al obtener la información del usuario: {str(e)}')

# Comando para solicitar la información del bot
@bot.command()
async def infobot(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["infobot"]
        color = discord.Colour.from_rgb(*color_tuple)

        bot_user = bot.user
        embed = discord.Embed(title="Información del Bot", color=color)
        embed.set_thumbnail(url=bot_user.avatar.url)
        embed.add_field(name="Nombre", value=bot_user.name, inline=False)
        embed.add_field(name="Versión", value="1.0", inline=False)
        embed.add_field(name="Creado por", value="Leonix64", inline=False)
        embed.add_field(name="Código fuente", value="[Enlace al código fuente](Proximamente...)", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al obtener la información del bot: {str(e)}')

# Comando para lanzar una moneda al azar
@bot.command()
async def moneda(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["moneda"]
        color = discord.Colour.from_rgb(*color_tuple)

        resultado = random.choice(["cara", "cruz"])

        # Crear un Embed para el resultado de la moneda
        embed = discord.Embed(title="Lanzamiento de Moneda", color=color)
        embed.add_field(name="Resultado", value=resultado, inline=False)
        embed.set_footer(text=f"Lanzado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        # Agregar una imagen de una moneda (cara o cruz) al Embed
        if resultado == "cara":
            embed.set_image(url="https://www.banxico.org.mx/multimedia/mon20_700anosMxTen_revPrensa.jpg")
        else:
            embed.set_image(url="https://www.banxico.org.mx/multimedia/anv_mon20Marina_prensaNgo.png")

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al tirar la moneda: {str(e)}')

# Comando para generar una contraseña segura
@bot.command()
async def clave_pass(ctx, longitud: int = 20):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["clave_pass"]
        color = discord.Colour.from_rgb(*color_tuple)

        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))

        # Crear un Embed para la contraseña segura
        embed = discord.Embed(title="Generador de Contraseña Segura", color=color)
        embed.add_field(name="Contraseña generada", value=f'||`{contrasena}`||', inline=False)
        embed.set_footer(text=f'Generada por {ctx.author.display_name}', icon_url=ctx.author.avatar.url)

        # Enviar el Embed en un mensaje privado al usuario
        await ctx.author.send(embed=embed)
        await ctx.send("¡Te he enviado tu contraseña por mensaje privado!")

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al generar la contraseña: {str(e)}')

# Comando para jugar a la ruleta rusa
@bot.command()
async def ruleta(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["ruleta"]
        color = discord.Colour.from_rgb(*color_tuple)

        chamber = random.randint(1, 6)
        trigger = random.randint(1, 6)

        # Crear un Embed para el juego de la ruleta
        embed = discord.Embed(title="Ruleta Rusa", color=color)
        embed.set_footer(text=f"Jugado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        if chamber == trigger:
            embed.add_field(name="¡BANG!", value="Parece que no sobreviviste. 😵💥", inline=False)
        else:
            embed.add_field(name="¡Click!", value="Sobreviviste por ahora. 😅🔫", inline=False)

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error, se trabó el revólver: {str(e)}')

# Comando para enviar un mensaje anónimo
@bot.command()
async def mensaje_anonimo(ctx, canal: discord.TextChannel, *, contenido):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["mensaje_anonimo"]
        color = discord.Colour.from_rgb(*color_tuple)

        # Crear un Embed para el mensaje anónimo
        embed = discord.Embed(title="Mensaje Anónimo", color=color)
        embed.add_field(name="Contenido del mensaje", value=contenido, inline=False)

        # Enviar el Embed en el canal especificado
        await canal.send(embed=embed)

        # Borrar el mensaje del autor del comando
        await ctx.message.delete()

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al enviar el mensaje: {str(e)}')

# Comando para enviar un mensaje en código morse
@bot.command()
async def morse(ctx, *mensaje):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["morse"]
        color = discord.Colour.from_rgb(*color_tuple)

        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', ' ': '/'
        }

        mensaje_morse = " ".join([morse_code_dict.get(c.upper(), c) for c in " ".join(mensaje)])

        # Crear un Embed para el mensaje en código Morse
        embed = discord.Embed(title="Mensaje en Código Morse", color=color)
        embed.add_field(name="Mensaje original", value=" ".join(mensaje), inline=False)
        embed.add_field(name="Mensaje en Morse", value=mensaje_morse, inline=False)
        embed.set_footer(text=f"Convertido por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al traducir: {str(e)}')

# Comando para realizar una prueba de latencia
@bot.command()
async def ping(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["ping"]
        color = discord.Colour.from_rgb(*color_tuple)

        latency = round(bot.latency * 1000)  # Convertir latencia a milisegundos

        # Crear un Embed para mostrar la latencia
        embed = discord.Embed(title="Ping del Bot", color=color)
        embed.add_field(name="Pong! Latencia", value=f"{latency} ms", inline=False)
        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al establecer la latencia: {str(e)}')

# Comando para solicitar la información del bot de servidores
@bot.command()
async def stats(ctx):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["stats"]
        color = discord.Colour.from_rgb(*color_tuple)

        total_users = len(bot.users)
        total_servers = len(bot.guilds)
        uptime = datetime.datetime.utcnow() - bot.user.created_at.replace(tzinfo=None)

        # Crear un Embed para mostrar las estadísticas del bot
        embed = discord.Embed(title="Estadísticas del Bot", color=color)
        embed.add_field(name="Usuarios totales", value=total_users)
        embed.add_field(name="Servidores totales", value=total_servers)
        embed.add_field(name="Tiempo en línea", value=str(uptime).split(".")[0])
        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error: {str(e)}')

# Comando para mostrar ayuda sobre los comandos disponibles
@bot.command()
async def ayuda(ctx, command_name: str = None):
    try:
        # Obtener el color correspondiente al comando
        color_tuple = color_Embed["ayuda"]
        color = discord.Colour.from_rgb(*color_tuple)

        if command_name:
            for command in commands_list:
                if command["name"] == command_name:
                    embed = discord.Embed(title=f"Comando: {command_name}", color=color)
                    embed.add_field(name="Descripción", value=command["description"], inline=False)
                    embed.add_field(name="Uso", value=command["usage"], inline=False)
                    await ctx.send(embed=embed)
                    return
            await ctx.send(f"No se encontró el comando '{command_name}'.")
        else:
            embed = discord.Embed(title="Comandos Disponibles", color=0x00ff00)
            for command in commands_list:
                embed.add_field(name=command["name"], value=command["description"], inline=False)
            await ctx.send(embed=embed)
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f'Error al obtener la ayuda del comando: {str(e)}')

@bot.command()
async def unirse(ctx):
    # Verifica si el autor del comando está en un canal de voz
    if ctx.author.voice is None:
        await ctx.send("Debes estar en un canal de voz para que el bot se una.")
        return

    # Obtén el canal de voz en el que se encuentra el autor del comando
    channel = ctx.author.voice.channel

    # Intenta unirse al canal de voz
    try:
        voice_client = await channel.connect()
        await ctx.send(f'El bot se ha unido al canal de voz: {channel.name}')
    except discord.ClientException as e:
        await ctx.send(f'Error al unirse al canal de voz: {e}')

    print('-------------------------------------------------------')

@bot.command()
async def salir(ctx):
    # Verifica si el bot está en un canal de voz
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send('El bot se ha desconectado del canal de voz.')

    print('-------------------------------------------------------')

# Iniciar el bot con el token
try:
    bot.run(TOKEN)
except Exception as e:
    print(f'Error al iniciar el bot: {e}')
