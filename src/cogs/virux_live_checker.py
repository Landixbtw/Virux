# TODO: eine liste in der DB die alle streamer speichert. 
# TODO: Eine möglichkeit die streamer zu löschen
# TODO: Einbindung der twitch api

channelName = []

contents = requests.get(f'https://www.twitch.tv/'+ {channelName}).content.decode('utf-8')

if 'isLiveBroadcast' in contents: 
    print(channelName + ' is live')
else:
    print(channelName + ' is not live')


import discord
from discord.ext import commands
from discord import ui, app_commands
import requests
import mariadb

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class virux_live_checker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Mache ein Embed")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(add_streamer="Which streamer would you like to add ?") # TODO: username ? or Link what input
    async def virux_live_checker(self, interaction: discord.Interaction):
       pass





async def setup(bot):
    await bot.add_cog(virux_live_checker(bot))
    print("virux_live_checker cog geladen ✔️")

