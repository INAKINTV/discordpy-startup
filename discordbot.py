from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.commands
async def /ping(ctx):
    await ctx.send('pong')
    
python bot.py

bot.run(NTgwOTQwOTU2Nzg3MDE1NzQw.XSVGFg.2OV_TLJkvJcPZG8tjXI4stGtHcA)
