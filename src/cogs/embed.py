import discord
from discord.ext import commands
from discord import app_commands
import logging

bot = commands.Bot(command_prefix="<", intents=discord.Intents.all())

class embed_maker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Mache ein Embed")
    #@app_commands.default_permissions(xxxx)
    @app_commands.describe(author="Autor")
    @app_commands.describe(title="Title")
    @app_commands.describe(body="Body")
    @app_commands.describe(images="Nur die URL des Bildes")
    async def embed_generator(self, interaction: discord.Interaction, author: str, title: str, body: str, images: str):
        try:
            embed = discord.Embed(
                title=f"{title}",
            )
            embed.set_author(name=f"{author}", url="")
            embed.set_image(url=f"{images}")
            
            embed.set_footer(text=f"Footer", icon_url="")
            
            await interaction.response.send_message(embed=embed)
        except Exception as err:
            logging.warning(err)



async def setup(bot):
    await bot.add_cog(embed_maker(bot))
    print("embed cog geladen ✔️")
