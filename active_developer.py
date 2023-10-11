# Importamos las bibliotecas necesarias
from discord import app_commands, Intents, Client, Interaction

# Creamos una clase Bot que hereda de la clase Client de Discord
class Bot(Client):
    def __init__(self, *, intents: Intents):
        # Inicializamos la clase padre con los intents proporcionados
        super().__init__(intents=intents)
        # Creamos un árbol de comandos para el bot
        self.tree = app_commands.CommandTree(self)

    # Método asíncrono para configurar el bot
    async def setup_hook(self) -> None:
        # Sincronizamos el árbol de comandos
        await self.tree.sync(guild=None)

# Creamos una instancia del bot con los intents predeterminados
bot = Bot(intents=Intents.default())

# Decorador para el evento `on_ready`, que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    # Imprimimos un mensaje indicando que el bot está conectado
    print(f"Conectado como: {bot.user}")

# Decorador para registrar el comando `givemebadge`
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    # Enviamos un mensaje al usuario indicando cómo reclamar la insignia
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

# Ejecutamos el bot con el token de autenticación
bot.run("Aqui_Pones_Tu_Token")


#Correrlo desde la terminal
# & "C:/Users/Alex Gonzalez/AppData/Local/Programs/Python/Python311/python.exe" "c:/Users/Alex Gonzalez/Documents/Codigos_Random/active_developer.py"