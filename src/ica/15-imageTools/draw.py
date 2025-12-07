from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *

def draw_something():
    # Create a blank canvas
    pic = Picture(600, 400)

    # Draw something cool here!
    # Example: Draw a simple smiley face

    # Face outline (yellow circle)
    pic.drawOval(150, 100, 450, 400, outlineColor="black", fillColor="yellow")

    # Left eye
    pic.drawOval(220, 180, 270, 230, outlineColor="black", fillColor="black")

    # Right eye
    pic.drawOval(330, 180, 380, 230, outlineColor="black", fillColor="black")

    # Smile (arc)
    pic.drawArc(220, 250, 380, 350, startAngle=0, endAngle=180,
                style='arc', outlineColor="black")

    return pic


def main():
    drawing = draw_something()
    drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()
