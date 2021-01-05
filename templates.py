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

    def render_meme(self):
        """
        Displays the meme to see
        """
        self.composition.show()

        return

    def get_result(self):
        return self.composition


class ImpactMeme(Meme):
    """
    Impact Font Memes use one image URL and consists of top and bottom text
    """
    def __init__(self):
        super().__init__()
        self.image_url = ''
        self.draw = None
        self.font_type = 'fonts/impact.ttf'

        return

    def set_image(self, url):
        """
        Grab the image from URL
        """
        self.image_url = url
        response = requests.get(self.image_url)
        self.composition = Image.open(BytesIO(response.content))
        self.draw = ImageDraw.Draw(self.composition)

        return

    def __get_font(self, text):

        # Get font size based on image width
        font_size = int(self.composition.size[0] / 10)

        # Set new font
        font = ImageFont.truetype(self.font_type, font_size)

        # Shrink size if text larger than width of image
        text_width, _ = self.draw.textsize(text, font=font)
        image_width, _ = self.composition.size
        while text_width >= (image_width * 0.95):
            font_size -= 1
            font = ImageFont.truetype(self.font_type, font_size)
            text_width, _ = self.draw.textsize(text, font=font)

        return font

    def set_toptext(self, top_text):
        font = self.__get_font(top_text)

        # Center text
        text_width, _ = self.draw.textsize(top_text, font=font)
        image_width, _ = self.composition.size
        x = (image_width - text_width) / 2
        y = 10

        self.__draw_outline_text(x=x, y=y, text=top_text, font=font)

        return

    def set_bottomtext(self, bottom_text):
        font = self.__get_font(bottom_text)

        # Center text
        text_width, text_height = self.draw.textsize(bottom_text, font=font)
        image_width, image_height = self.composition.size
        x = (image_width - text_width) / 2
        y = image_height - text_height - 10

        self.__draw_outline_text(x=x, y=y, text=bottom_text, font=font)

        return

    def __draw_outline_text(self, x, y, text, font):
        """
        Add signature outline to Impact Font
        """
        # Determine black border based on font height
        stroke_width = int(font.getsize(text)[1] / 15)

        self.draw.text((x, y), text, fill=(0, 0, 0),
                       font=font, stroke_width=stroke_width)
        self.draw.text((x, y), text, fill=(255, 255, 255), font=font)

        return
