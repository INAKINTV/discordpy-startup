
from discord.ext import commands
import os
import traceback

client = discord.Client() #ガンかも

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event #ここから
async def on_reaction_add(reaction, user):
   # author: リアクションがついたメッセージを書いた人
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")



@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def 募集(ctx):
    await ctx.send('参加者を募集します')



bot.run(token)
