# Meme Templates

from PIL import Image, ImageFont, ImageDraw, ImageSequence
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
        """
        Returns the edited image as a BytesIO object
        """
        arr = BytesIO()
        if getattr(self.composition, "is_animated", False):
            self.composition.save(
                arr, format=self.composition.format, save_all=True)
        else:
            self.composition.save(arr, format=self.composition.format)
        arr.seek(0)
        return arr


class ImpactMeme(Meme):
    """
    Impact Font Memes use one image URL and consists of top and bottom text
    """

    def __init__(self):
        super().__init__()
        self.image_url = ''
        self.font_type = 'fonts/impact.ttf'
        return

    def set_image(self, url):
        """
        Grab the image from URL
        """
        self.image_url = url
        response = requests.get(self.image_url)
        self.composition = Image.open(BytesIO(response.content))
        return

    def __get_font(self, text):
        draw = ImageDraw.Draw(self.composition)
        # Get font size based on image width
        font_size = int(self.composition.size[0] / 10)

        # Set new font
        font = ImageFont.truetype(self.font_type, font_size)

        # Shrink size if text larger than width of image
        text_width, _ = draw.textsize(text, font=font)
        image_width, _ = self.composition.size
        while text_width >= (image_width * 0.95):
            font_size -= 1
            font = ImageFont.truetype(self.font_type, font_size)
            text_width, _ = draw.textsize(text, font=font)
        return font

    def set_toptext(self, top_text):
        font = self.__get_font(top_text)
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, _ = draw.textsize(top_text, font=font)
        image_width, _ = self.composition.size
        x = (image_width - text_width) / 2
        y = 0

        self.__draw_outline_text(x=x, y=y, text=top_text, font=font)
        return

    def set_bottomtext(self, bottom_text):
        font = self.__get_font(bottom_text)
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, text_height = draw.textsize(bottom_text, font=font)
        image_width, image_height = self.composition.size
        x = (image_width - text_width) / 2
        y = (image_height - text_height) * 0.96

        self.__draw_outline_text(x=x, y=y, text=bottom_text, font=font)
        return

    def __draw_outline_text(self, x, y, text, font):
        """
        Add signature outline to Impact Font
        """
        # Determine black border based on font height
        stroke_width = int(font.getsize(text)[1] / 15)

        frames = []
        for i, frame in enumerate(ImageSequence.Iterator(self.composition)):

            if frame.mode != 'RGB' and frame.mode != 'RGBA':
                frame = frame.convert('RGBA')

            draw = ImageDraw.Draw(frame)
            draw.text((x, y), text, fill=(0, 0, 0),
                      font=font, stroke_width=stroke_width)
            draw.text((x, y), text, fill=(255, 255, 255), font=font)

            arr = BytesIO()
            frame.save(arr, format=self.composition.format)
            frame = Image.open(arr)

            frames.append(frame)

        arr = BytesIO()
        if getattr(self.composition, "is_animated", False):
            frames[0].save(arr, format=self.composition.format,
                           save_all=True, append_images=frames[1:])
        else:
            frames[0].save(arr, format=self.composition.format)
        self.composition = Image.open(arr)
        return


class PosterMeme(Meme):
    """
    Poster Memes use one image URL and creates a black border motivational poster
    """

    def __init__(self):
        super().__init__()
        self.image_url = ''
        self.top_font_type = 'fonts/times-new-roman.ttf'
        self.bottom_font_type = 'fonts/ARIAL.ttf'
        self.image_height = 0
        return

    def set_image(self, url):
        """
        Grab the image from URL, then add black border
        """
        def add_thin_border(thickness, color):
            image_width, image_height = self.composition.size
            border_thickness = max(image_width, image_height) * thickness
            border_width = int(image_width + 2 * border_thickness)
            border_height = int(image_height + 2 * border_thickness)

            # Ensure borders are centered
            if (border_width - image_width) % 2 == 1:
                border_width += 1
            if (border_height - image_height) % 2 == 1:
                border_height += 1

            border = Image.new(mode='RGB', size=(
                border_width, border_height), color=color)
            border.paste(self.composition, (int(
                (border_width - image_width) / 2), int((border_height - image_height) / 2)))
            border.format = self.composition.format
            return border

        def add_thick_border(thickness):
            image_width, image_height = self.composition.size
            self.border_thickness = max(image_width, image_height) * 0.065
            border_width = int(image_width + 2 * self.border_thickness)
            border_height = int(image_height + 2 * self.border_thickness)

            # Ensure borders are centered
            if (border_width - image_width) % 2 == 1:
                border_width += 1
            if (border_height - image_height) % 2 == 1:
                border_height += 1

            border = Image.new(mode='RGB', size=(
                border_width, border_height + int(self.border_thickness * 2)), color=(0, 0, 0))
            border.paste(self.composition, (int(
                (border_width - image_width) / 2), int((border_height - image_height) / 2)))
            border.format = self.composition.format
            return border

        self.image_url = url
        response = requests.get(self.image_url)
        self.composition = Image.open(BytesIO(response.content))

        self.composition = add_thin_border(thickness=0.005, color=(0, 0, 0))
        self.composition = add_thin_border(
            thickness=0.003, color=(255, 255, 255))
        self.image_height = self.composition.size[1]
        self.composition = add_thick_border(thickness=0.07)

        return

    def set_toptext(self, top_text):
        font = ImageFont.truetype(
            self.top_font_type, int(self.border_thickness * 2))
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, _ = draw.textsize(top_text, font=font)
        image_width, _ = self.composition.size
        x = (image_width - text_width) / 2
        y = self.image_height + self.border_thickness

        draw.text((x, y), top_text, fill=(255, 255, 255), font=font)
        return

    def set_bottomtext(self, bottom_text):
        font = ImageFont.truetype(
            self.bottom_font_type, int(self.border_thickness / 2))
        draw = ImageDraw.Draw(self.composition)

        # Center text
        text_width, _ = draw.textsize(bottom_text, font=font)
        image_width, _ = self.composition.size
        x = (image_width - text_width) / 2
        y = int(self.image_height + self.border_thickness * 3)

        draw.text((x, y), bottom_text, fill=(255, 255, 255), font=font)
        return
