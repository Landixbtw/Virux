import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import mariadb
import sys 
import aiohttp
import re

from helpcommand import MyHelp

load_dotenv()
token = str(os.getenv("TOKEN"))

handler = logging.Handler()
# NOTE: Bot prefix " ! "
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class bot(commands.Bot):
    def __init__(self,):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

 #   bot.load_extension("embed_command")

    # NOTE: This loads only the cogs aka. Slash Commands
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

    async def on_guild_join(self, guild):
    # NOTE: This function is called as soon as the bot joins a server 
    # this dynamically creates a table. For each guild. Uneccessary here because the Bot is only
    # deployed on one server but who cares.

        table_prefix =f"guild_{guild.id}"

        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {table_prefix}_STREAMERS (USERNAME TEXT)"
        )
        
        con.commit()
    
    async def on_guild_remove(self, guild):
        # NOTE: This function is called when the bot is removed from the guild
        
        table_prefix = f"guild_{guild.id}"

        cur.execute(f"DROP TABLE IF EXISTS {table_prefix}_STREAMERS")


try:
    con = mariadb.connect(
        user="ole",
        password="QrsoL82",
        host="192.168.10.183",
        port=3306,
        database="virux_esports",
    )
    
except mariadb.Error as mariaErr:
    print(f"Error connecting to MariaDB Platform: {mariaErr}")
    sys.exit(1)

cur = con.cursor()

bot = bot()


# WARNING: !!!!!!!!!!!!!!

# NOTE: This is the Embed prefix command

async def get_image_size(url):
    async with aiohttp.ClientSession() as session:
        async with session.head(url) as response:
            if response.status == 200:  # Check if the request was successful
                size = response.headers.get('Content-Length')
                return int(size) if size else 0
            else:
                return 0  # In case the request fails, return 0 as the size

# Your existing create_embed command here, which now includes the get_image_size function
@bot.command()
async def create_embed(ctx, author: str, body: str, *image_urls: str, thumbnail_url: str = None):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)'  # domain...
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if len(image_urls) > 4:
        await ctx.send("Error: You can provide a maximum of 4 images.")
        return

    if thumbnail_url and not re.match(url_regex, thumbnail_url):
        await ctx.send("Error: The provided thumbnail URL is invalid.")
        return

    for url in image_urls:
        if not re.match(url_regex, url):
            await ctx.send(f"Error: The provided image URL '{url}' is invalid.")
            return

    async def get_image_sizes(image_urls):
        sizes = []
        for url in image_urls:
            size = await get_image_size(url)
            sizes.append(size)
        return sizes

    # Get the sizes asynchronously and then sum them
    sizes = await get_image_sizes(image_urls)
    total_size = sum(sizes)
    
    if total_size > 25 * 1024 * 1024:  # 25 MB in bytes
        await ctx.send("Error: The combined size of the images exceeds 25MB.")
        return

    embed = discord.Embed(title=author, description=body, color=discord.Color.blue())
    for url in image_urls:
        embed.add_image(url=url)

    if thumbnail_url:
        embed.set_thumbnail(url=thumbnail_url)

    await ctx.send(embed=embed)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send(f'An error occurred: {str(error)}')

#WARNING: !!!!!!!!!!!!!!!!!!

rules_keywords = ["rules", "regeln", "┃regeln", "⚖-rules", ]
welcome_keyword = ["welcome", "willkommen", "👋🏼｜welcome"]

fortnite_keyword = ["📩┃fortnite-apply",]
cod_keyword = ["📩┃cod-apply",]
valorant_keyword = ["📩┃valorant-apply",]

@bot.event
async def on_member_join(member: discord.Member):
    # NOTE: ↓↓ TEST SERVER GUILD ID
    specific_guild = bot.get_guild(1156981897956688033) # WARNING: CHANGE GUILD IT
    
    for keyword in rules_keywords:
        rules_channel = discord.utils.get(specific_guild.channels, name=keyword)
        if rules_channel:
            break  # Stop searching if a matching channel is found
    
    for keyword in welcome_keyword: 
        welcome_channel = discord.utils.get(specific_guild.channels, name=keyword)
        if welcome_channel:
            break
    
    for keyword in fortnite_keyword:
        fortnite_apply = discord.utils.get(specific_guild.channels, name=keyword)
        if fortnite_apply:
            break
        else:
            print(f"Couldnt find {fortnite_apply}")
    for keyword in cod_keyword:
        cod_apply = discord.utils.get(specific_guild.channels, name=keyword)
        if cod_apply:
            break
        else: 
            print(f"Couldnt find {cod_apply}")

    for keyword in valorant_keyword:
        valorant_apply = discord.utils.get(specific_guild.channels, name=keyword)
        if valorant_apply:
            break
        else:
            print(f"Couldnt find {valorant_apply}")


    if welcome_channel:
        if rules_channel:
            try:
                await welcome_channel.send(f"{member.mention} Welcome! \nLies dir bitte die {rules_channel.mention} durch, wenn du dich bewerben möchtest, dann öffne gerne unser Bewerbungssystem unter, {fortnite_apply.mention}, {valorant_apply.mention} ")
            except discord.HTTPException as e:
                print(f"Error sending welcome message: {e}")  # Handle potential errors
        else: 
            await welcome_channel.send(f"**Error:** *Errorcode 1* Please report this to the maintainer. ") # WARNING: ERROR CODE 1: rules channel doesnt exist or isnt correclty written
            print("rules channel not found in the specified guild.")
    else:
        print("welcome channel not found in the specified guild. Check channel name, permissions, and asynchronous behavior.")


# Dictionary to store channels created for members
member_channels = {}

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(1156981897956688033)  # Your guild ID
    join_for_voice = discord.utils.get(guild.voice_channels, name="join_for_voice")

    # Member joins the join_for_voice channel
    if after.channel == join_for_voice:
        # Create a new voice channel for the member
        try:
            new_channel = await guild.create_voice_channel(name=f"{member}", category=join_for_voice.category, user_limit=5, reason=f"Automatic creation for {member}")
            print(f"Created new voice channel: {new_channel.name}")

            # Move member to the new channel and store the channel ID
            await member.move_to(new_channel, reason="Custom Channel move")
            member_channels[new_channel.id] = member.id  # Store the channel with the member's ID
        except discord.HTTPException as e:
            print(f"Error creating voice channel: {e}")

    # Member leaves a channel
    if before.channel and before.channel.id in member_channels:
        # Check if the channel is empty
        if len(before.channel.members) == 0:
            # Delete the channel if empty
            await before.channel.delete(reason="Automatic deletion after member left")
            del member_channels[before.channel.id]  # Remove the channel from the tracking dictionary



bot.help_command = MyHelp()

bot.run(token)
