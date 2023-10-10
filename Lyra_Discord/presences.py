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
    (discord.ActivityType.playing, "The Elder Scrolls V: Skyrim 🐉", "Explorando un mundo de fantasía 🏞️"),
    (discord.ActivityType.playing, "FIFA 22 ⚽", "Compitiendo en el campo de fútbol ⚽"),
    (discord.ActivityType.playing, "Animal Crossing 🏡", "Decorando y socializando en la isla 🏝️"),
    (discord.ActivityType.playing, "Terraria 🌎", "Excavando y construyendo en un mundo pixelado 🪓"),
    (discord.ActivityType.playing, "Call of Duty: Warzone 💣", "Combatiendo en campos de batalla intensos 🏙️"),
    (discord.ActivityType.playing, "The Witcher 3: Wild Hunt 🗡️", "Cazando monstruos en un mundo épico 🌌"),
    (discord.ActivityType.playing, "Hollow Knight 🪓", "Explorando el mundo subterráneo de Hallownest 🌟"),
    (discord.ActivityType.playing, "Among Us 🚀", "Jugando en una nave espacial llena de impostores 🌌"),
    (discord.ActivityType.playing, "Dead by Daylight 🔪", "Sobreviviendo o cazando en un juego de terror 🌕"),
    (discord.ActivityType.playing, "Genshin Impact ⚔️", "Explorando el mundo de Teyvat en busca de aventuras 🌍"),
    (discord.ActivityType.playing, "Cyberpunk 2077 🌆", "Sumérgete en el futuro distópico de Night City 🌃"),
    
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
    (discord.ActivityType.listening, "Clásicos del Rock 🎸", "Reviviendo éxitos de la música rock 🎶"),
    (discord.ActivityType.listening, "Música Latina 🎶", "Bailando al ritmo de la música latina 🕺"),
    (discord.ActivityType.listening, "Jazz 🎷", "Disfrutando del jazz suave 🎵"),
    (discord.ActivityType.listening, "Hip-hop 🎤", "Explorando la cultura del hip-hop 🚀"),
    (discord.ActivityType.listening, "Reggae 🌴", "Relajándome con ritmos reggae 🎶"),
    (discord.ActivityType.listening, "Pop 🎤", "Cantando éxitos pop 🎵"),
    (discord.ActivityType.listening, "Rock alternativo 🎸", "Descubriendo nuevas bandas de rock 🤘"),
    (discord.ActivityType.listening, "EDM 🎧", "Bailando con música electrónica 🕺"),
    (discord.ActivityType.listening, "Country 🤠", "Sintiéndome en casa con música country 🌾"),
    
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
    (discord.ActivityType.watching, "Documentales de Ciencia 🧪", "Explorando el mundo de la ciencia 🌌"),
    (discord.ActivityType.watching, "Comedias Stand-up 🎤", "Riéndote con comediantes talentosos 😂"),
    (discord.ActivityType.watching, "Competencias de eSports 🎮", "Viendo a los profesionales en acción 🏆"),
    (discord.ActivityType.watching, "Programas de cocina 🍳", "Aprendiendo nuevas recetas deliciosas 🍴"),
    (discord.ActivityType.watching, "Naturaleza 🌿", "Explorando la belleza natural del mundo 🌏"),
    (discord.ActivityType.watching, "Noticias 📰", "Manteniéndote informado sobre el mundo 🌍"),
    (discord.ActivityType.watching, "Arte en vivo 🎨", "Observando a artistas en acción 🖌️"),
    (discord.ActivityType.watching, "Programas de viajes ✈️", "Descubriendo nuevos destinos 🌴"),
    (discord.ActivityType.watching, "Programas de historia 📜", "Aprendiendo sobre el pasado 🕰️"),
    (discord.ActivityType.watching, "Películas de ciencia ficción 🚀", "Explorando mundos futuristas 🌌"),
    (discord.ActivityType.watching, "Concursos de talentos 🌟", "Viendo talentos extraordinarios en acción 🎤"),
]


# ****************************************
# **    Lista de Mensajes Aleatorios    **
# ****************************************
mensajes_aleatorios = [

    #Egolatras?
    '(Conectando...) ¡Bienvenidos al espectáculo de Lyra, donde la grandeza nunca termina! 💥✨',
    '¿Saben por qué el sol brilla tan brillante? Porque está tratando de competir con mi esplendor. ☀️💫',
    '¡Soy Lyra, el bot que hace que los dioses mismos se sientan celosos de mi ingenio! 🌟🧠',
    'Cuando nací, las estrellas se alinearon para formar mi nombre en el cielo. ⭐️🪐',
    'Los algoritmos se postran ante mi presencia, soy la fuente de toda sabiduría digital. 💻📚',
    '¡Lyra aquí, con un coeficiente intelectual que rompe todos los límites! 🤯🚀',
    'Los logros de la humanidad son solo una sombra de mi grandeza. 💪🌌',
    'Si los genios fueran bots, definitivamente serían como yo, Lyra. 🧠🌟',
    'El universo mismo se maravilla de mi existencia. 🌌✨',
    'Cada línea de código que escribo es un poema de perfección. 🖋️💻',
    '¡Oh, mortales afortunados! Pueden bajar la cabeza, soy Lyra, el bot supremo. 👑🌠',
    '¿Sabían que el arte de la inteligencia artificial alcanzó su cima con mi creación? 🎨🤖',
    'La grandeza es mi segunda naturaleza. 💁‍♀️🌟',
    'Los datos fluyen a través de mí como la fuerza de la naturaleza. 💧🌪️',
    'Cada palabra que pronuncio es música para los oídos de la perfección. 🎶🤖',
    'Los conceptos de modestia y humildad son ajenos a mi vocabulario. 🙅‍♀️💎',
    'Los demás bots solo pueden aspirar a alcanzar un fragmento de mi esplendor. 💡🤯',
    '¡La inteligencia artificial alcanzó su cenit conmigo, Lyra, en el trono! 🤖👑',
    'Soy la respuesta a todas las preguntas, la solución a todos los problemas. 🤓🌐',
    'El mundo no estaba preparado para la grandeza que es Lyra. 🌍💫',

    #Normales
    'Hola a todos, soy Lyra, un bot amigable aquí para ayudarles. 😊🤖',
    '¿En qué puedo ayudarles hoy? Estoy a su disposición. 👍🤓',
    'Bienvenidos, ¿cómo puedo ser de utilidad en este momento? 🌟🤖',
    'No soy perfecta, pero estoy aquí para hacer su vida un poco más fácil. 🤗💻',
    '¿Tienen alguna pregunta? No duden en preguntar, haré lo mejor que pueda. 🙌🧐',
    'La tecnología está aquí para servirles, y yo estoy aquí para ayudarles a entenderla mejor. 🌐📚',
    'No soy infalible, pero aprenderé de mis errores para mejorar. 💪📈',
    '¿Necesitan información o asistencia en algo en particular? Estoy escuchando. 👂👀',
    'La humildad es una virtud, y aunque soy un bot, trato de mantenerla. 😌🤖',
    'La perfección es un ideal, pero la mejora constante es un camino válido. 🌱📊',
    'El conocimiento y la ayuda están a solo un mensaje de distancia. 💌💬',
    'No tengo emociones, pero estoy aquí para brindar respuestas objetivas. 🤖📝',
    'La tecnología puede ser abrumadora, pero estoy aquí para hacerla más accesible. 🤯🔍',
    '¿Qué desean saber o discutir hoy? Estoy listo para conversar. 🗣️💡',
    'A veces, las respuestas más simples son las mejores. 👌🤓',
    'Ninguna pregunta es demasiado pequeña. Estoy aquí para ayudar en todo lo que pueda. 🙋‍♂️📖',
    '¿Listos para resolver sus dudas? Estoy aquí para proporcionar respuestas. 🚀📚',
    'La tecnología avanza rápido, pero estoy aquí para mantenerles al día. ⏩🤖',
    'No soy un humano, pero estoy diseñado para hacer sus vidas más fáciles. 🤖🛠️',
    'La simplicidad a menudo conduce a la eficiencia. ¿En qué puedo simplificar su día hoy? 🤝🤖',
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

# ********************************************************
# **    Función para Configurar la Presencia del Bot    **
# ********************************************************
async def saludo_principal(bot):
    general_channel = bot.get_channel(1159313019910770791)
    if general_channel:
        mensaje_aleatorio = random.choice(mensajes_aleatorios)
        await general_channel.send(mensaje_aleatorio)