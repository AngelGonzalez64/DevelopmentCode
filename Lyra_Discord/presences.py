import discord
import random
import asyncio
import time

# *********************************************
# **    Lista de Actividades Predefinidas    **
# *********************************************
actividades = [
    # Jugando
    (discord.ActivityType.playing, "Juegos reales 🎮", "Divirtiéndome en servidores 🕹️"),
    (discord.ActivityType.playing, "Minecraft 🌍", "Construyendo y explorando 🪓"),
    (discord.ActivityType.playing, "Among Us 🚀", "¡Buscando al impostor! 🔍"),
    (discord.ActivityType.playing, "Fortnite 🔫", "Construyendo y disparando 🏰"),
    (discord.ActivityType.playing, "League of Legends ⚔️", "Luchando en la Grieta del Invocador 🏟️"),
    (discord.ActivityType.playing, "Rocket League ⚽", "Marcando goles en el coche 🚗"),
    (discord.ActivityType.playing, "Valorant 🔫", "Disparando enemigos en un futuro cercano 🌆"),
    (discord.ActivityType.playing, "Apex Legends 🪖", "Luchando en el Cañón de los Reyes 🏞️"),
    (discord.ActivityType.playing, "Overwatch 💥", "Defendiendo o atacando en equipos 🧑‍🤝‍🧑"),
    (discord.ActivityType.playing, "Stardew Valley 🚜", "Gestionando tu granja 🌾"),
    
    # Escuchando
    (discord.ActivityType.listening, "Música 🎵", "Tocando algunas canciones 🎶"),
    (discord.ActivityType.listening, "Podcasts 🎙️", "Escuchando temas interesantes 📻"),
    (discord.ActivityType.listening, "Audiolibros 📚", "Explorando mundos a través de palabras 🌍"),
    (discord.ActivityType.listening, "ASMR 🤫", "Relajándome con sonidos suaves 🌊"),
    (discord.ActivityType.listening, "Radio en línea 📻", "Sintonizando emisoras en vivo 🎙️"),
    (discord.ActivityType.listening, "Sonidos de la naturaleza 🌿", "Disfrutando de la tranquilidad 🌄"),
    (discord.ActivityType.listening, "Metallica 🤘", "Escuchando mis canciones favoritas 🎸"),
    (discord.ActivityType.listening, "Lo-fi hip-hop 🎧", "Estudiando con música relajante 📖"),
    (discord.ActivityType.listening, "SoundCloud 🎶", "Descubriendo nuevos artistas 🎤"),
    (discord.ActivityType.listening, "Bandcamp 🎵", "Apoyando a músicos independientes 🎤"),
    
    # Viendo
    (discord.ActivityType.watching, "Peliculas 🎥", "Disfrutando de una película 🍿"),
    (discord.ActivityType.watching, "Series de TV 📺", "Siguiendo tramas emocionantes 🍿"),
    (discord.ActivityType.watching, "YouTube 📹", "Viendo videos interesantes 🎞️"),
    (discord.ActivityType.watching, "Twitch 📺", "Observando transmisiones en vivo 🕹️"),
    (discord.ActivityType.watching, "Animé 🍥", "Explorando mundos animados 🌸"),
    (discord.ActivityType.watching, "Documentales 📼", "Aprendiendo cosas nuevas 📚"),
    (discord.ActivityType.watching, "Conciertos en línea 🎤", "Disfrutando de actuaciones en vivo 🎵"),
    (discord.ActivityType.watching, "Deportes en TV 📺", "Apoyando a tu equipo favorito 🏀"),
    (discord.ActivityType.watching, "Netflix 🍿", "Viendo series exclusivas 📺"),
    (discord.ActivityType.watching, "Disney+ 🐭", "Disfrutando de contenido de Disney 🏰"),
]

# ********************************************************
# **    Función para Configurar la Presencia del Bot    **
# ********************************************************
async def set_bot_presence(bot):
    while True:
        # Elegir una actividad al azar de la lista
        actividad = random.choice(actividades)
        
        custom_presence = discord.Activity(
            type=actividad[0],
            name=actividad[1],
            state=actividad[2],
        )
        
        await bot.change_presence(
            activity=custom_presence,
            status=discord.Status.online
        )
        
        # Esperar un tiempo para cambiar de estado nuevamente (segundos)
        await asyncio.sleep(1800)
