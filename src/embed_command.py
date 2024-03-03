import discord
from discord.ext import commands

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycommand(self, ctx, author: str, body: str, *, images: typing.List[str] = None):
        embed = discord.Embed(
            title="Your Title Here",
            description=body,
            color=discord.Color.blue()
        )
        embed.set_author(name=author)

        # Add images to the embed
        if images:
            for index, image_url in enumerate(images[:4]):
                embed.set_image(url=image_url)

        # Add optional thumbnail
        # embed.set_thumbnail(url="URL TO THUMBNAIL IMAGE")

        # Add optional footer
        # embed.set_footer(text="Your Footer Text Here")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCommand(bot))
