import discord 
from discord.ext import commands
from discord import ui

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

class apply(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=86400)
        self.value = None
     
    answer_team = ui.TextInput(label="Für welches Team möchtest du dich bewerben ?", style=discord.TextStyle.short,placeholder="placeholder test", default="", required= True, max_length=15)
    answer_rules = ui.TextInput(label="Hast du dir unsere Regeln durchgelesen ?", style=discord.TextStyle.short, placeholder="Ja", default="Nein", required=True, max_length=5)
    answer_age = ui.TextInput(label="Wie alt bist du", style=discord.TextStyle.short, placeholder="ALTER", default="", required=True, max_length=3)
    answer_attention = ui.TextInput(label="Wie bist du auf uns aufmerksam geworden ? ", style=discord.TextStyle.short, placeholder="Instagram", default="", required=False,  max_length=50)
    answer_goals = ui.TextInput(label="Hast du Ziele ? Wenn ja, welche ?", style=discord.TextStyle.short, placeholder="", default="", required=False, max_length=50)
    answer_why_us = ui.TextInput(label="Was erhoffst du dir bei uns ?", style=discord.TextStyle.short, placeholder="", default="", required=True, max_length=99)
    answer_gametag = ui.TextInput(label="Epic/Valorant/CoD Name, evtl. Fortnite Tracker, Valorant Tracker, CoD Tracker.", style=discord.TextStyle.short, placeholder="Gamertag", default="", required=True, max_length=20)


    @discord.ui.button(label="Report", style=discord.ButtonStyle.red)
    async def report(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        apply_channel = discord.utils.get(guild.channels)

        if apply_channel == "Bewerbung":
           await interaction.response.send_modal() # 
       
