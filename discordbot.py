#coding:utf-8
token = "NTgwOTQwOTU2Nzg3MDE1NzQw.XSWSYg.w4YtTF5ohWxuLKSFnYeUuLu4H_I"                                                                                                         22
    
import discord
import discord.client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']



@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

# サインアップ(未定)

# 募集
@bot.command()
async def 募集(ctx):
    await ctx.send('募集を開始します')


    
    
    
bot.run(token)
