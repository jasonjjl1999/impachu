# Impachu meme maker

from PIL import Image, ImageFont, ImageDraw 
import requests
from io import BytesIO

class Meme:
    """
    The basic meme object
    """
    def __init__(self):
        self.composition = None

        return

    """
    Displays the meme to see
    """
    def render_meme(self):
        self.composition.show()

        return

    def get_result(self):
        return self.composition

class ImpactMeme(Meme):
    def __init__(self):
        """
        Impact Font Memes use one image URL and consists of top and bottom text
        """
        super().__init__()
        self.image_url = ''
        self.top_text = ''
        self.bottom_text = ''
        self.font_size = 100
        self.font_type = 'fonts/impact.ttf'
        self.font = ImageFont.truetype(self.font_type, self.font_size)

        return

    def set_image(self, url):
        """
        Grab the image from URL
        """
        self.image_url = url
        response = requests.get(self.image_url)
        self.composition = BytesIO(response.content)
        self.composition = Image.open(self.composition)

        return

    def set_fontsize(self, size):
        self.font_size = size
        self.font = ImageFont.truetype(self.font_type, self.font_size)

        return

    def set_toptext(self, text):
        self.top_text = text
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, _ = draw.textsize(self.top_text, font=self.font)
        image_width, _ = self.composition.size
        x = (image_width - text_width) / 2
        y = 10

        self.__draw_outline_text(draw=draw, x=x, y=y, text=self.top_text, font=self.font) 

        return

    def set_bottomtext(self, text):
        self.bottom_text = text
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, text_height = draw.textsize(self.bottom_text, font=self.font)
        image_width, image_height = self.composition.size
        x = (image_width - text_width) / 2
        y = image_height - text_height - 10

        self.__draw_outline_text(draw=draw, x=x, y=y, text=self.bottom_text, font=self.font)

        return

    def __draw_outline_text(self, draw, x, y, text, font):
        """
        Add signature outline to Impact Font
        """
        draw.text((x-1, y), text, fill=(0, 0, 0), font=font)
        draw.text((x+1, y), text, fill=(0, 0, 0), font=font)
        draw.text((x, y-1), text, fill=(0, 0, 0), font=font)
        draw.text((x, y+1), text, fill=(0, 0, 0), font=font)
        draw.text((x, y), text, fill=(255, 255, 255), font=font)  

        return
