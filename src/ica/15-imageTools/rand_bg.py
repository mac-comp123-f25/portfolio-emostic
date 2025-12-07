import time
import random
from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *


def get_rand_bg():
    # Generate random values for the red, green, and blue channels (0-255)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    random_color = (r, g, b)

    # Create a blank 100x100 picture
    bg_picture = Picture(100, 100)

    # Set all pixels to the generated random color
    bg_picture.setAllPixels(random_color)

    return bg_picture



def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
