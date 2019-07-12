from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ねこ(ctx):
    await ctx.send('にゃーん')

    
@bot.command()
async def @5(ctx):
    await ctx.send('@5だよ～')
    
    
@bot.command()
async def @4(ctx):
    await ctx.send('@4だよ～')
    
    @bot.command()
async def @3(ctx):
    await ctx.send('@3だよ～')

    @bot.command()
async def @2(ctx):
    await ctx.send('@2だよ～')

@bot.command()
async def @1(ctx):
    await ctx.send('@1だよ～')

@bot.command()
async def 〆(ctx):
    await ctx.send('〆だよ～')








bot.run(token)


