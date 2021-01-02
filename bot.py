import os
from io import BytesIO
import discord
import shlex
from dotenv import load_dotenv

import impachu

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event 
async def on_message(message):

    # Prevent bot calling itself
    if message.author == client.user:
        return

    if message.content.startswith('--helpachu'):
        await help_command(message)

    if message.content.startswith('--impact'):
        await impact_command(message)


async def help_command(message):
    await message.channel.send("""
    Buongiorno! I am Impachu.

    **• helpachu**: Help
        Usage: `--helpachu`\n
    **• impact**: Impact meme maker
        Usage: `--impact <URL> "<Top Text>" "<Bottom Text>"`\n""")

    return

async def impact_command(message):
    """
    Bot Response for '--impact' command
    format:
        --impact <URL> "<Top Text>" "<Bottom Text>"
    """

    top_text = ''
    bottom_text = ''
    url_valid = False

    # Parse Parameters
    params = shlex.split(message.content)
    url = params[1]
    top_text = params[2]
    if len(params) >= 4:
        bottom_text = params[3]

    edited_meme = impachu.make_impact_meme(image_url=url, top_text=top_text, bottom_text=bottom_text)
    result_image = edited_meme.get_result()

    await message.channel.send("Happy New Year!")
    arr = BytesIO()
    result_image.save(arr, format='PNG')
    arr.seek(0)
    await message.channel.send(file=discord.File(fp=arr, filename='meme.png'))

    return


client.run(TOKEN)
