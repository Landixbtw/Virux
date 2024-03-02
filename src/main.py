import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import datetime

from helpcommand import MyHelp

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
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"𝙑𝙞𝙧𝙪𝙭 eSports"))

bot = bot()

@bot.event


@bot.event
async def on_member_join(member: discord.Member):
    # NOTE: ↓↓ TEST SERVER GUILD ID
    specific_guild = bot.get_guild(1156981897956688033) # WARNING: CHANGE GUILD IT

    welcome_channel = discord.utils.get(specific_guild.channels, name="welcome")

    if welcome_channel:
        try:
            await welcome_channel.send(f"Hey, {member.mention}, Willkommen bei 𝙑𝙞𝙧𝙪𝙭 eSports!")
        except discord.HTTPException as e:
            print(f"Error sending welcome message: {e}")  # Handle potential errors
    else:
        print("Welcome channel not found in the specified guild. Check channel name, permissions, and asynchronous behavior.")




# Dictionary to store the first member who joined each channel
first_member = {}

@bot.event
async def on_voice_state_update(member, before, after):
    # Get the specific guild where you want to create voice channels
    guild = bot.get_guild(1156981897956688033)  # Change to your guild ID
    
    # Get the "join_for_voice" channel
    join_for_voice = discord.utils.get(guild.voice_channels, name="join_for_voice")
    
    # Check if the member joined the "join_for_voice" channel
    if after.channel and after.channel == join_for_voice:
        print(f"{member} joined the voice channel: {after.channel.name}")
        
        # Store the first member who joined the channel
        if join_for_voice.id not in first_member:
            first_member[join_for_voice.id] = member
    
        # Create a new voice channel for the member
        try:
            new_channel = await guild.create_voice_channel(name=f"{member}", category=join_for_voice.category, user_limit=5, reason=f"Automatic creation for {join_for_voice}")
            print(f"Created new voice channel: {new_channel.name}")
        except discord.HTTPException as e:
            print(f"Error creating voice channel: {e}")

    # Check if the member left the channel
    if before.channel and before.channel == join_for_voice:
        print(f"{member} left the voice channel: {before.channel.name}")
        
        # Check if the member who initially joined has left
        if before.channel.id in first_member:
            original_member = first_member[before.channel.id]
            if original_member == member:
                # Delete the channel if the initial member has left
                channel_name = f"{member}"
                channel = discord.utils.get(guild.voice_channels, name=channel_name)
                if channel:
                    await channel.delete(reason=f"Original member {member} left the channel")
                    print(f"Deleted voice channel: {channel.name}")
                else:
                    print(f"Voice channel not found: {channel_name}")
                del first_member[before.channel.id]


bot.help_command = MyHelp()

bot.run(token)
