import discord
from discord.ext import commands
import traceback

# *****************************************************
# **    Comando para Eliminar un Rol del Servidor    **
# *****************************************************

# Define una función que configure los comandos relacionados con roles
def Eliminar_Rol(bot):
    @bot.command()
    async def eliminar_rol(ctx, rol: discord.Role):
        try:
            # Verifica si el autor tiene permisos para administrar roles
            if ctx.author.guild_permissions.manage_roles:
                # Elimina el rol del servidor
                await rol.delete()

                # Crear un Embed informativo
                embed = discord.Embed(
                    title="Rol Eliminado",
                    description=f"¡El rol '{rol.name}' ha sido eliminado con éxito!"
                )

                await ctx.send(embed=embed)
            else:
                await ctx.send("No tienes permisos para eliminar roles en este servidor.")
        except discord.Forbidden:
            await ctx.send("No tengo permisos para eliminar roles o el rol que intentas eliminar es superior al mío.")
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al eliminar el rol: {str(e)}')
