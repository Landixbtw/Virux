# Slash Command for application.

import discord
from discord.ext import commands
from discord import app_commands
import datetime
import logging

bot = commands.Bot(command_prefix="<", intents=discord.Intents.all())

class apply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="Bewerbung", description="Bewerbe dich bei uns!")
    @app_commands.describe(Alter="Wie alt bist du? ")
    @app_commands.describe(Spiel="Für welches Spiel willst du dich bewerben? ")
    @app_commands.describe(Rank="Welcher Rank/Elo bist du? ")

    async def apply(self, interaction: discord.Interaction, Alter: str, Spiel: str, Rank: str):
    
        now = datetime.datetime.now()
        current_time = now.strftime('%H:%M:%S')
        nummer = 0;
        nummer++:
        
        try:
            embed = discord.Embed(title=f"Bewerbung von {interaction.user.name}", description="")
            embed.set_author(name=f"Bewerbung #{nummer}", url=f"{interaction.user.global_name}", icon_url="")
            embed.add_field(name="**Alter:** ", value=f"{Alter}", inline=False)
            embed.add_field(name="**Spiel:** ", value=f"{Spiel}", inline=False)
            embed.add_field(name="**Rank:** ",  value=f"{Rank}", inline=False)
            
            await interaction.response.send_message("Deine Bewerbung wurde eingereicht. Es wird sich jemand bei dir melden.")
            # TODO: Bot schickt die Bewerbung in einen Channel ?
