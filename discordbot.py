from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
end

@bot.command()
async def 草(ctx):
    await ctx.send('草')
end






bot.run(NTgwOTQwOTU2Nzg3MDE1NzQw.XSh_lg.YQJNaoIsJM9FNtX387vKMqt5xZM)


