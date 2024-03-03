import discord
from discord.ext import commands
from discord import app_commands


STREAMER_LIST = []
PHRASE_LIST = []

class StreamerManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="add_streamer", description="Add a streamer to the list.")
    @app_commands.describe(streamer_name="The name of the streamer to add.")
    async def add_streamer(self, interaction: discord.Interaction, streamer_name: str):
        STREAMER_LIST.append(streamer_name)
        print("Added streamer to list")
        print(STREAMER_LIST)
        # Logic to add the streamer
        await interaction.response.send_message(f"Streamer {streamer_name} added to the list.")

    @app_commands.command(name="remove_streamer", description="Remove a streamer from the list.")
    @app_commands.describe(streamer_name="The name of the streamer to remove.")
    async def remove_streamer(self, interaction: discord.Interaction, streamer_name: str):
        STREAMER_LIST.remove(streamer_name)
        print("Removed streamer from list")
        print(STREAMER_LIST)
        # Logic to remove the streamer
        await interaction.response.send_message(f"Streamer {streamer_name} removed from the list.")

    @app_commands.command(name="add_phrase", description="Add a phrase to the announcements.")
    @app_commands.describe(phrase="The phrase to add.")
    async def add_phrase(self, interaction: discord.Interaction, phrase: str):
        PHRASE_LIST.append(phrase)
        print("Added phrase to list")
        print(PHRASE_LIST)
        # Logic to add the phrase
        await interaction.response.send_message(f"Phrase '{phrase}' added to the announcements.")

    @app_commands.command(name="remove_phrase", description="Remove a phrase from the announcements.")
    @app_commands.describe(phrase="The phrase to remove.")
    async def remove_phrase(self, interaction: discord.Interaction, phrase: str):
        PHRASE_LIST.remove(phrase)
        print("Removed phrase from list")
        print(PHRASE_LIST)
        # Logic to remove the phrase
        await interaction.response.send_message(f"Phrase '{phrase}' removed from the announcements.")

async def setup(bot):
    await bot.add_cog(StreamerManagement(bot))
    print("Streamer Management cog loaded ✔️")

