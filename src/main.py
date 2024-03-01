import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import datetime

load_dotenv()
token = str(os.getenv("TOKEN"))

handler = logging.Handler()
# NOTE: Bot prefix
bot = commands.Bot(command_prefix="<", intents=discord.Intents.all())

class bot(commands.Bot):
    def __init__(self,):
        super().__init__(command_prefix="<", intents=discord.Intents.all())

    async def setup_hook(self):
        print("loading cogs...")
        for file in os.listdir("./cogs/"):
            if file.endswith(".py"):
                try:
                    name = file[:-3]
                    await bot.load_extension(f"cogs.{name}")
                except Exception as cogErr:
                    print(f"error: {cogErr}")

    async def on_ready(self):
        print(f"{bot.user.name} is ready to rumble!")
        print("Published by Moritz Henri Reiswaffel III")
        try: 
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands!")
        except Exception as syncErr:
            print(f"error: {syncErr}")

        print("-------------------")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name(f"𝙑𝙞𝙧𝙪𝙭 eSports")))


bot = bot()

@bot.event
async def on_member_join(member: discord.Member):
    await channel.send(f"Hey, {member.mentioned}, Willkommen bei 𝙑𝙞𝙧𝙪𝙭 eSports")


bot.help_command = MyHelp()

bot.run(token, logging_handler=handler)
