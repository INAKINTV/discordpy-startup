    
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

# サインアップ(未定)

# 募集
@bot.command()
async def /募集(ctx):
    await ctx.send('募集を開始します')

    @client.event
async def hoge()

    
    
    
bot.run(token)
