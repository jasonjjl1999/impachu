import os
from io import BytesIO
import discord
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

    # Respond to command only
    if message.content.startswith('--impact'):

        top_text = ''
        bottom_text = ''
        url_valid = False

        for param in message.content.split():
            if param.startswith('url'):
                url = param.split('=')[1]
                url_valid = True
            if param.startswith('top'):
                top_text = param.split('=')[1]
            if param.startswith('bottom'):
                bottom_text = param.split('=')[1]

        if not url_valid:
            print ("Image URL missing")
            return False

        edited_meme = impachu.make_impact_meme(image_url=url, top_text=top_text, bottom_text=bottom_text)
        result_image = edited_meme.get_result()

        await message.channel.send("Happy New Year!")
        arr = BytesIO()
        result_image.save(arr, format='PNG')
        arr.seek(0)
        await message.channel.send(file=discord.File(fp=arr, filename='meme.png'))

client.run(TOKEN)