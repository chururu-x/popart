"""
File: warhol.py
----------------
This program converts portraits to Andy Warhol's pop art style.
It converts pixels above a certain brightness threshold to one
color, and pixels below a certain threshold to another.
There are 4 different filters to choose from.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed

from simpleimage import SimpleImage
from PIL import Image
from math import sqrt

# image source: https://unsplash.com/s/photos/portrait
# partial color scheme from: https://design.tutsplus.com/tutorials/how-to-make-a-warhol-pop-art-effect-in-photoshop--cms-31060

# defines brightness thresholds
BRIGHTNESS_THRESHOLD_1 = 130
BRIGHTNESS_THRESHOLD_2 = 50

# RGB values of Group 1 colors (name: candy)
YELLOW = (255, 255, 49)
HOT_PINK = (252, 11, 114)
TURQUOISE_GREEN = (11, 255, 183)

# RGB values of Group 2 colors (name: sizzle)
MAGENTA = (255, 48, 254)
COBALT_BLUE = (12, 96, 255)
AMBER = (255, 207, 11)

# RGB values of Group 3 colors (name: party)
CYAN = (1, 255, 255)
BRIGHT_RED = (249, 3, 3)
LIME_GREEN = (148, 255, 17)

# RGB values of Group 4 colors (name: dance)
SKY_BLUE = (112, 186, 255)
NEON_PINK = (254, 8, 121)
NAVY = (0, 55, 179)

# RGB values of Group 5 pop art colors (name: rocknroll)
VIOLET = (106, 0, 255)
MANGO = (251, 202, 7)
RED = (254, 0, 0)

def main():
    # print intro message
    intro = get_intro_message()

    # asks user to choose a number from 1 to 15
    choice = int(input('Enter a number from 1 to 16: '))
    if choice > 16:
        choice = int(input("Pls enter a number from 1 to 16: "))
    # Get file and load image
    filename = get_file(choice)
    image = SimpleImage(filename)

    # Show the original fire
    original_portrait = SimpleImage(filename)
    # original_portrait.show()

    # Choose color scheme
    color_scheme = input("Would you like to: candy, sizzle, party, dance or rocknroll? Please choose one: ")
    print("loading...")
    # Show image with Warhol filter
    warhol_portrait = add_filter(filename, color_scheme)
    warhol_portrait.show()

def get_intro_message():
    print("Choose your Warhol avatar!")
    return get_intro_message

def get_file(choice):
    # Read image file path from user, or use the default file
    if choice == 1:
        filename = 'images/portrait1.jpeg'
    if choice == 2:
        filename = 'images/portrait2.jpeg'
    if choice == 3:
        filename = 'images/portrait3.jpeg'
    if choice == 4:
        filename = 'images/portrait4.jpeg'
    if choice == 5:
        filename = 'images/portrait5.jpeg'
    if choice == 6:
        filename = 'images/portrait6.jpeg'
    if choice == 7:
        filename = 'images/portrait7.jpeg'
    if choice == 8:
        filename = 'images/portrait8.jpeg'
    if choice == 9:
        filename = 'images/portrait9.jpeg'
    if choice == 10:
        filename = 'images/portrait10.jpeg'
    if choice == 11:
        filename = 'images/portrait11.jpeg'
    if choice == 12:
        filename = 'images/portrait12.jpeg'
    if choice == 13:
        filename = 'images/portrait13.jpeg'
    if choice == 14:
        filename = 'images/portrait14.jpeg'
    if choice == 15:
        filename = 'images/portrait15.jpeg'
    if choice == 16:
        filename = 'images/portrait16.jpeg'
    return filename

def add_filter(filename, color_scheme):
    """
    This function converts pixels below or above a certain
    threshold to a certain color.
    """
    image = Image.open(filename)
    width = image.width
    height = image.height
    color_dict = get_color_scheme(color_scheme)
    for y in range(height):
        for x in range(width):
            color = image.getpixel((x, y))
            # find brightness of pixel
            brightness_average = (color[0] + color[1] + color[2]) // 3
            # converts pixels above brightness threshold to YELLOW
            if brightness_average > BRIGHTNESS_THRESHOLD_1:
                image.putpixel((x, y), color_dict.get("color_1"))
            # converts pixels below brightness threshold to HOT PINK
            elif brightness_average < BRIGHTNESS_THRESHOLD_1 and brightness_average > BRIGHTNESS_THRESHOLD_2:
                image.putpixel((x, y), color_dict.get("color_2"))
            else:
                image.putpixel((x, y), color_dict.get("color_3"))

    # remember to return the image
    return image

def get_color_scheme(color_scheme):
    color_dict = {}
    if color_scheme == "candy":
        color_dict = {"color_1": YELLOW, "color_2": HOT_PINK, "color_3": TURQUOISE_GREEN}
    if color_scheme == "sizzle":
        color_dict = {"color_1": MAGENTA, "color_2": COBALT_BLUE, "color_3": AMBER}
    if color_scheme == "party":
        color_dict = {"color_1": CYAN, "color_2": BRIGHT_RED, "color_3": LIME_GREEN}
    if color_scheme == "dance":
        color_dict = {"color_1": SKY_BLUE, "color_2": NEON_PINK, "color_3": NAVY}
    if color_scheme == "rocknroll":
        color_dict = {"color_1": VIOLET, "color_2": MANGO, "color_3": RED}
    return color_dict


if __name__ == '__main__':
    main()
