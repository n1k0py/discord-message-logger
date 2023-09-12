import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print('Python Code Has Been Started To Log Messages As {0.user}'.format(bot))
    print("Bot Will Collect Every Single Message In Every Single Server's Channel If Bot Have Permission")

@bot.event
async def on_message(message):
    try:
        print('==============================================')
        print(message.author.name + " said:")
        print(message.content)
        print('In ' + message.guild.name)
        print('==============================================')
    except Exception as e:
        print(f"An error occurred: {e}")

bot.run('TOKEN_ HERE!')
