import  math
def rect_area(width, length):
    """THis calculates the area of a rectangle with width and length"""
    area = width * length
    return area
rect_area(20,40)
def roof_cost(area,sqf_cost):
    """This function calculates the roof cost given area and sqf cost"""
    costt=area*sqf_cost
    return costt
roof_cost(60,40)
def estimate_green_roof(width, length, sqf_cost):
    """This function estimates the green roof cost given area and sqf cost"""
    width = math.ceil(width)
    "converts the width value to integer"
    length = math.ceil(length)
    "converts the length value to integer"
    area = rect_area(width, length)

    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

estimate_green_roof(32.8,54.25,35)