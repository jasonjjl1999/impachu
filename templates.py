# Impachu meme maker

from PIL import Image, ImageFont, ImageDraw 
import requests
from io import BytesIO

class Meme:
    """
    The basic meme object
    """
    def __init__(self):
        self.image = None

    """
    Displays the meme to see
    """
    def render_meme(self):
        meme = Image.open(self.image)
        meme.show()

class ImpactMeme(Meme):
    def __init__(self):
        """
        Impact Font Memes use one image URL and consists of top and bottom text
        """
        super().__init__()
        self.image_url = ''
        self.top_text = ''
        self.bottom_text = ''

    def set_image(self, url):
        """
        Grab the image from URL
        """
        self.image_url = url
        response = requests.get(self.image_url)
        self.image = BytesIO(response.content)

