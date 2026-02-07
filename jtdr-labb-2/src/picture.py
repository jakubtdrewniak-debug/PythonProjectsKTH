"""Displays a Sierpinski Fractal."""
from tkinter import *
from random import randint


__author__ = "Marcus Dicander"
__copyright__ = "Copyright 2019-2024, Kth"
__license__ = "CC0"


"""The width and height of the image. Change these values to change the size of the image.
Make sure to use normalized coordinates for each function call to make sure the image scales
properly when the width and height are changed."""
WIDTH = 800
HEIGHT = 600


def normalized_to_pixel(n: float) -> int:
    """Converts a normalized value to a pixel value."""
    return int(n * WIDTH)


def pixel_to_normalized(p: int) -> float:
    """Converts a pixel value to a normalized value."""
    return p / WIDTH


def sierpinski(img, color="#ff00ff"):
    """Adds a Sierpinski Fractal to img and returns None."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x & y == 0:
                img.put(color, (x, y))


def random_shape(img, upper_left: tuple[float, float], lower_right: tuple[float, float], color: str="#ffffff"):
    """Draws a random shape in img with the given color. The coordinates are normalized and given
    in the order (x, y) for the upper left and lower right corners of the shape.
    This implementation uses a random number generator to decide if a pixel should be colored or not.
    Your functions should have similar signatures to this one. Feed the image and the normalized
    coordinates to the function and make it draw the requested shape for each task. You may use
    the functions normalized to pixel and pixel to normalized to convert between the two coordinate
    systems."""
    for y in range(normalized_to_pixel(upper_left[1]), normalized_to_pixel(lower_right[1])):
        for x in range(normalized_to_pixel(upper_left[0]), normalized_to_pixel(lower_right[0])):
            if randint(0, 1) == 0:
                img.put(color, (x, y))


def main():
    """Create your image and call your functions from here"""
    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    """Below this comment is where you should put your function calls to draw things
    in the Canvas. Do not change the code above this comment. Do not call mainloop 
    outside of this function."""
    sierpinski(img, "#ff00ff")
    random_shape(img, (0.8, 0.2), (0.97, 0.83), "#ff0000")
    """Do not change any code below this comment."""
    mainloop()


if __name__ == '__main__':
    main()
