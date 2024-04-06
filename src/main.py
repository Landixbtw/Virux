from types import prepare_class
import discord
from discord import ui
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

from helpcommand import MyHelp


load_dotenv()
token = str(os.getenv("TOKEN"))

handler = logging.Handler()
# NOTE: Bot prefix " ! "
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


class bot(commands.Bot):
    def __init__(
        self,
    ):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    #   bot.load_extension("embed_command")
    #
    # # NOTE: This loads only the cogs aka. Slash Commands
    # async def setup_hook(self):
    #     print("loading cogs...")
    #     for file in os.listdir("./cogs/"):
    #        if file.endswith(".py"):
    #             try:
    #                 name = file[:-3]
    #                 await bot.load_extension(f"cogs.{name}")
    #             except Exception as cogErr:
    #                 print(f"error: {cogErr}")
    #
    async def on_ready(self):
        print(f"{bot.user.name} is ready to rumble!")
        print("Published by Moritz Henri Reiswaffel III")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands!")
        except Exception as syncErr:
            print(f"error: {syncErr}")
        print("-------------------")
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.streaming, name=f"𝙑𝙞𝙧𝙪𝙭 eSports"
            )
        )


bot = bot()


class ApplicationModal(ui.Modal, title="Bewerbung für 𝙑𝙞𝙧𝙪𝙭 eSports"):

    answer_team = ui.TextInput(
        label="Für welches Team möchtest du dich bewerben ?",
        style=discord.TextStyle.long,
        placeholder="Fortnite/Valorant/CoD",
        required=True,
        max_length=15,
    )
    answer_age = ui.TextInput(
        label="Wie alt bist du",
        style=discord.TextStyle.short,
        placeholder="Alter",
        required=True,
        max_length=3,
    )
    answer_goals = ui.TextInput(
        label="Hast du Ziele? Wenn ja, welche ?",
        style=discord.TextStyle.long,
        max_length=200,
    )
    answer_why_us = ui.TextInput(
        label="Was erhoffst du dir bei uns ?",
        style=discord.TextStyle.long,
        required=True,
        max_length=200,
    )
    answer_gamer_tag = ui.TextInput(
        label="Epic/Valorant/CoD Name & Tracker",
        style=discord.TextStyle.long,
        placeholder="Epic/Valorant/CoD Name & Tracker",
        required=True,
        max_length=20,
    )

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        apply_channel = discord.utils.get(guild.text_channels, name="bewerbungen")

        # Construct the message from the modal's input fields
        embed = discord.Embed(
            title=f"Bewerber: {interaction.user.name} UserID: {interaction.user.id}"
        )
        embed.add_field(
            name="Für welches Team möchtest du dich Bewerben ?:",
            value=f"**{self.answer_team}**",
            inline=False,
        )
        embed.add_field(
            name="Wie alt bist du ?:", value=f"**{self.answer_age}**", inline=False
        )
        embed.add_field(name=" ?:", value=f"**{self.answer_goals}**", inline=False)
        embed.add_field(
            name="Was erhoffst du dir bei uns ?",
            value=f"**{self.answer_why_us}**",
            inline=False,
        )
        embed.add_field(
            name="Epic/Valorant/CoD Name, evtl. Fortnite Tracker, Valorant Tracker, CoD Tracker:",
            value=f"**{self.answer_gamer_tag}**",
            inline=False,
        )

        # Check if the 'bewerbungen' channel was found
        if apply_channel:
            # Send the constructed message to the 'bewerbungen' channel
            await apply_channel.send(embed=embed)

            # Acknowledge the interaction
            await interaction.response.send_message(
                "Deine Bewerbung wurde eingereicht, Viel Glück!", ephemeral=True
            )
        else:
            # In case the 'bewerbungen' channel is not found, send a response to the user
            await interaction.response.send_message(
                f"Error: Application Channel could not be found. Please Create a channel called [bewerbungen], or make sure the bot has access to the existing one."
            )


class SimpleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="apply", style=discord.ButtonStyle.success, custom_id="apply_button"
    )
    # TODO: Nur admins können den button spawnen
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ApplicationModal()
        await interaction.response.send_modal(modal)


@bot.command()
async def button(ctx):
    view = SimpleView()
    # view.add_item(button)
    await ctx.send(view=view)


rules_keywords = [
    "┃regeln",
    "rules",
    "regeln",
    "⚖-rules",
]
welcome_keyword = [
    "👋🏼｜welcome",
    "welcome",
    "willkommen",
]

fortnite_keyword = [
    "📩｜fortnite-apply",
]
cod_keyword = [
    "📩｜cod-apply",
]
valorant_keyword = [
    "📩｜valorant-apply",
]


@bot.event
async def on_member_join(member: discord.Member):
    specific_guild = bot.get_guild(862307078282412062)  # WARNING: REAL GUILD ID

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
                with open("./Virux_eSports_-_Twitter_Header.jpg", "rb") as f:
                    picture = discord.File(f)
                await welcome_channel.send(
                    f"{member.mention} Welcome! \nLies dir bitte die {rules_channel.mention} durch, wenn du dich bewerben möchtest, dann öffne gerne unser Bewerbungssystem unter, {fortnite_apply.mention}, {valorant_apply.mention}"
                )
                await welcome_channel.send(file=picture)
            except discord.HTTPException as e:
                print(f"Error sending welcome message: {e}")  # Handle potential errors
        else:
            await welcome_channel.send(
                f"**Error:** *Errorcode 1* Please report this to the maintainer. "
            )  # WARNING: ERROR CODE 1: rules channel doesnt exist or isnt correclty written
            print("rules channel not found in the specified guild.")
    else:
        print(
            "welcome channel not found in the specified guild. Check channel name, permissions"
        )


# NOTE: join_for_voice

# Dictionary to store channels created for members
member_channels = {}


@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(862307078282412062)  # WARNING: REAL GUILD ID
    join_for_voice = discord.utils.get(guild.voice_channels, name="join_for_voice")

    # Member joins the join_for_voice channel
    if after.channel == join_for_voice:
        # Create a new voice channel for the member
        try:
            new_channel = await guild.create_voice_channel(
                name=f"{member}",
                category=join_for_voice.category,
                user_limit=5,
                reason=f"Automatic creation for {member}",
            )
            print(f"Created new voice channel: {new_channel.name}")

            # Move member to the new channel and store the channel ID
            await member.move_to(new_channel, reason="Custom Channel move")
            member_channels[new_channel.id] = (
                member.id
            )  # Store the channel with the member's ID
        except discord.HTTPException as e:
            print(f"Error creating voice channel: {e}")

    # Member leaves a channel
    if before.channel and before.channel.id in member_channels:
        # Check if the channel is empty
        if len(before.channel.members) == 0:
            # Delete the channel if empty
            await before.channel.delete(reason="Automatic deletion after member left")
            del member_channels[
                before.channel.id
            ]  # Remove the channel from the tracking dictionary


bot.help_command = MyHelp()

bot.run(token)
