import discord
from discord.ext import commands
from config import TOKEN,PREFIX
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=PREFIX,intents=discord.Intents.all(), case_insensitive=True, self_bot=True,application_id='1081811927396790313')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to my users"))
    await bot.tree.sync()

    try:
      # Load the extensions (cogs)
      await bot.load_extension("cogs.moderation")
      await bot.load_extension("cogs.modmail")
      await bot.load_extension("cogs.ticket")
      await bot.load_extension("cogs.utility")
      await bot.load_extension("cogs.fun")
      await bot.load_extension("cogs.weather")
      await bot.load_extension("cogs.translate")

    except Exception as e:
        print(f'Error loading extension: {e}')
    
@bot.tree.command(name='ping',description='Returns the bots latency')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency: {round(bot.latency * 1000)}ms")



keep_alive()
# Start the bot
bot.run(TOKEN)
