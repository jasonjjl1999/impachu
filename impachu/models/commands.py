import discord
from discord.ext import commands
from impachu.models.templates import GANsNRoses


class Models(commands.Cog, name='Memes'):
    """
    Commands for using various types of AI-models
    """
    @commands.command(name='anime',
                      help='Uses facial recognition to turn your face into anime')
    async def impact(self, ctx, url):
        """
        Command for using GANsNRoses Neural Network
        """
        ai_inference = GANsNRoses()
        ai_inference.run_inference(url)
        result_image = ai_inference.get_result()

        await ctx.send(file=discord.File(fp=result_image, filename='meme.gif'))
        return
    