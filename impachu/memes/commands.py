import discord
from discord.ext import commands
from impachu.memes.templates import ImpactMeme, PosterMeme

class Memes(commands.Cog, name='Memes'):
    """
    Commands for making various types of memes
    """
    @commands.command(name='impact', aliases=['impachu'],
                      help='Adds impact font to any image to create a meme')
    async def impact(self, ctx, url, top_text='', bottom_text=''):
        """
        Command for making impact format memes
        """
        impact_meme = ImpactMeme()
        impact_meme.set_image(url)
        impact_meme.set_toptext(top_text)
        impact_meme.set_bottomtext(bottom_text)
        result_image = impact_meme.get_result()

        await ctx.send(file=discord.File(fp=result_image, filename='meme.gif'))
        return

    @impact.error
    async def impact_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(error)
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error executing command, please try again (Check that URL is valid).')
        else:
            await ctx.send('Error executing command, please try again.')
        return

    @commands.command(name='poster',
                      help='Adds (de)motivational poster format to any image')
    async def poster(self, ctx, url, top_text='', bottom_text=''):
        """
        Command for making poster format memes
        """
        poster_meme = PosterMeme()
        poster_meme.set_image(url)
        poster_meme.set_toptext(top_text)
        poster_meme.set_bottomtext(bottom_text)

        result_image = poster_meme.get_result()
        await ctx.send(file=discord.File(fp=result_image, filename='meme.gif'))
        return