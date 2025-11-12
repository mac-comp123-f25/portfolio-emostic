def weighted_scale(pic, w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = w1 * r + w2 * g + w3 * b
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

def negative (pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        neg_r = 255 -r
        neg_g = 255 - g
        neg_b = 255 - b
        new_pic.setColor(x, y, (neg_r, neg_g, neg_b))
    return new_pic
