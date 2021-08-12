import os
import sys
import discord
from dotenv import load_dotenv
from discord.ext import commands
from pretty_help import PrettyHelp

from impachu.memes.commands import Memes
from impachu.models.commands import Models

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN == None:
    print('Failed to acquire token, did you create the .env file with your discord key?')
    sys.exit(1)

# Initialize bot
bot = commands.Bot(
    command_prefix='!',
    description='Buongiorno! I am Impachu. :zap:',
    case_insensitive=True,
    help_command=PrettyHelp())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Set Activity
    activity = discord.Game(name='!help', type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    return


bot.add_cog(Memes())
bot.add_cog(Models())

def main():
    bot.run(TOKEN, bot=True)
