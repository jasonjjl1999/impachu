import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from pretty_help import PrettyHelp

from impachu.memes.commands import Memes

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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

def main():
    bot.run(TOKEN, bot=True)
