import discord

bot = commands.Bot()
@bot.event
async def on_ready():
    print('Python Code Has Been Sterted To Log Messages As {0.user}'.format(bot))
    print("Bot Will Collect Every Single Message In Every Single Server's Channel If Bot Have Permission")

@client.event
async def on_message(message):
  print('==============================================')
  print(message.author.name
