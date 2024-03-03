from discord.ext import commands

class StreamerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.streamers = {}  # key: streamer name, value: live status

    @commands.slash_command(description="Add a streamer to the watch list")
    async def add_streamer(
        self,
        ctx,
        streamer_name: Option(str, "Enter the streamer's name")
    ):
        if streamer_name in self.streamers:
            await ctx.respond(f"{streamer_name} is already in the list.")
        else:
            self.streamers[streamer_name] = False  # Initially set to not live
            await ctx.respond(f"Added {streamer_name} to the streamer list.")

    @commands.slash_command(description="Remove a streamer from the watch list")
    async def remove_streamer(
        self,
        ctx,
        streamer_name: Option(str, "Enter the streamer's name")
    ):
        if streamer_name in self.streamers:
            del self.streamers[streamer_name]
            await ctx.respond(f"Removed {streamer_name} from the streamer list.")
        else:
            await ctx.respond(f"{streamer_name} is not in the list.")

def setup(bot):
    bot.add_cog(StreamerCommands(bot))
