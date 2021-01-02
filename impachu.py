import templates

def main():

    make_impact_meme()


def make_impact_meme(image_url, font_size, top_text, bottom_text):

    my_meme = templates.ImpactMeme()
    my_meme.set_image(image_url)
    my_meme.set_fontsize(font_size)
    my_meme.set_toptext(top_text)
    my_meme.set_bottomtext(bottom_text)
    my_meme.render_meme()

    return

if __name__ == '__main__':

    main()