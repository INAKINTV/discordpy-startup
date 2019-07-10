
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']





@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def 募集(ctx):
    await ctx.send('参加者を募集します')



bot.run(token)
