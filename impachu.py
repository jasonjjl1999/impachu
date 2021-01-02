import templates

def main():

    make_impact_meme()


def make_impact_meme(image_url, top_text, bottom_text, font_size=0):

    my_meme = templates.ImpactMeme()
    my_meme.set_image(image_url)
    my_meme.set_toptext(top_text)
    my_meme.set_bottomtext(bottom_text)

    return my_meme

if __name__ == '__main__':

    main()