from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.commands
async def /neko(ctx):
    await ctx.send('にゃーん')
    
    @bot.commands
async def /ねこ(ctx):
    await ctx.send('にゃーん')


bot.run(token)
