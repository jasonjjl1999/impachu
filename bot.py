import os
import shlex
from io import BytesIO
from dotenv import load_dotenv

import discord
from discord.ext import commands
from pretty_help import PrettyHelp

import util

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


class Memes(commands.Cog, name='Memes'):
    """
    Commands for making memes
    """
    @commands.command(name='impachu',
                      help='Adds impact font to any image to create a meme')
    async def impact_command(self, ctx, url, top_text='', bottom_text=''):
        """
        Command for making impact format memes
        """

        edited_meme = util.make_impact_meme(
            image_url=url, top_text=top_text, bottom_text=bottom_text)
        result_image = edited_meme.get_result()

        await ctx.send(file=discord.File(fp=result_image, filename='meme.gif'))

        return


bot.add_cog(Memes())
bot.run(TOKEN, bot=True)
