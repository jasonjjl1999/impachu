import os
from io import BytesIO
import discord
from discord.ext import commands
import shlex
from dotenv import load_dotenv

import impachu

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(
    command_prefix='!',
    description='Boungiorno! I am Impachu.')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
        
    # Set Activity
    activity = discord.Game(name="!helpachu", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    return


@bot.command(
    name='impachu', 
    help='Adds impact font to any image to create a meme')
async def impact_command(ctx, url, top_text, bottom_text=''):
    """
    Bot Response for '--impact' command
    format:
        --impact <URL> "<Top Text>" "<Bottom Text>"
    """

    edited_meme = impachu.make_impact_meme(image_url=url, top_text=top_text, bottom_text=bottom_text)
    result_image = edited_meme.get_result()

    await ctx.send("Happy New Year!")
    arr = BytesIO()
    result_image.save(arr, format='PNG')
    arr.seek(0)
    await ctx.send(file=discord.File(fp=arr, filename='meme.png'))

    return

bot.run(TOKEN, bot=True)
