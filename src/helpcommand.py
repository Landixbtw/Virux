import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96

class MyHelp(commands.HelpCommand):
    #&help
    async def send_bot_help(self, mapping):
        await self.context.send("Dieser Bot ist zur Unterstützung es Virux eSports Teams da. \n\n Bei Fragen rund zum Bot fragt Entweder das Server team. Oder auf diesem Server: https://discord.gg/Ryd5uz7J2n")
