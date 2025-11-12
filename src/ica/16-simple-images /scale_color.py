from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic1 = Picture("../SampleImages/blueBird.jpg")

def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

def weighted_scale(pic, w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = w1 * r + w2 * g + w3 * b
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

gray_pic = grayscale(pic1)
gray_pic.save("../SampleImages/blueBird.jpg")
gray_pic.explore()

keep_windows_open()
