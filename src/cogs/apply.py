import discord
from discord.ext import commands
from discord import ButtonStyle, ui, app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    
class ApplyButton(discord.ui.Button):
    def __init__(self, *args, **kwargs):
        # Initialize the button with predefined style, label, and emoji
        super().__init__(style=discord.ButtonStyle.secondary, label="Apply", emoji="📝", *args, **kwargs)


        async def callback(self, interaction: discord.Interaction):
        # This method is called when the button is clicked.
        # You can respond to the click in various ways, such as sending a message.
            await interaction.response.send_message("You clicked the apply button!", ephemeral=True)

class MyView(discord.ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the ApplyButton to this view
        self.add_item(ApplyButton())

class setup_apply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="setup_apply", description="Mache ein Embed")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(apply_channel="In what channel would you like people to apply")
    async def ticket_system_setup(self, interaction: discord.Interaction, apply_channel: discord.TextChannel):
        pass
        
        if not apply_channel:
            await interaction.response.send_message(f"The channel {apply_channel} does not exists")
        
        if apply_channel:
            await interaction.response.send_message("Click the button to apply", view=MyView())

async def setup(bot):
    await bot.add_cog(setup_apply(bot))
    print("apply cog geladen ✔️")
