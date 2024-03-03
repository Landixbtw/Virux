from discord.ext import commands
from discord.commands import Option

class PhraseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.phrases = ["Streamer is now live! Check them out here:"]  # Default phrase

    @commands.slash_command(description="Add a phrase to the announcement list")
    async def add_phrase(
        self,
        ctx,
        phrase: Option(str, "Enter the phrase")
    ):
        self.phrases.append(phrase)
        await ctx.respond("Added new phrase.")

    @commands.slash_command(description="Remove a phrase from the announcement list")
    async def remove_phrase(
        self,
        ctx,
        phrase: Option(str, "Enter the phrase")
    ):
        if phrase in self.phrases:
            self.phrases.remove(phrase)
            await ctx.respond("Removed phrase.")
        else:
            await ctx.respond("Phrase not found.")

def setup(bot):
    bot.add_cog(PhraseCommands(bot))
