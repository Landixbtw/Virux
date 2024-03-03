import discord
from discord.ext import commands
from discord import ui, app_commands
import logging

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class ticket_system_setup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Mache ein Embed")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(support_category="Please select the category you want to use, Application and Support")
    async def ticket_system_setup(self, interaction: discord.Interaction, support_category: discord.CategoryChannel, apply_category: discord.CategoryChannel):
        
        guild = interaction.guild
        


        # NOTE: Check for categories

        # NOTE: Category for -- Tickets made, Tickets closed  
        # NOTE: Channel for ticket buttons, open, apply
        # NOTE: In support ticket embed with "message" -- buttons close, reopen ?, delete --> EMBED MESSAGE PIN 
        # NOTE: Logs für ticket geöffnet und geschlossen ?
        # NOTE: Channel for transcript
        #
        # NOTE: Für bewerbungs ticket ein apply button, andere kategorei, modal bei Ticket öffnung. Gleiche buttons, transcript etc
async def setup(bot):
    await bot.add_cog(ticket_system_setup(bot))
    print("ticket_system_setup cog geladen ✔️")

