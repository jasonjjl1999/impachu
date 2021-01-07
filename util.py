import templates


def main():

    pass

def make_impact_meme(image_url, top_text, bottom_text):

    my_meme = templates.ImpactMeme()
    my_meme.set_image(image_url)
    my_meme.set_toptext(top_text)
    my_meme.set_bottomtext(bottom_text)
    return my_meme


def make_poster_meme(image_url, top_text, bottom_text):

    my_meme = templates.PosterMeme()
    my_meme.set_image(image_url)
    my_meme.set_top_text(top_text)
    my_meme.set_bottom_text(bottom_text)
    return my_meme


if __name__ == '__main__':

    main()
