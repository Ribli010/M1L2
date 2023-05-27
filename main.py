import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run("MTEwOTM4NDY1ODgyNDcyNDU0MA.GF7_iA.4WGZW8Oe46yckxdDe9x3MtCvg0LIKZTAyv0SeE")
