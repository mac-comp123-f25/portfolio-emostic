from picture import Picture

def colorShuffle(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (b, r, g))
    return new_pic

mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
