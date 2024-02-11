import math
from dip import *

"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
          Perform image flipping along horizontal or vertical direction

          image: the input image to flip
          direction: direction along which to flip

          return: output_image
          """

        # Solve The assignment flipping
        newArray = array(image)

        if direction == "horizontal":
            output_image = newArray[:, ::-1, :]  # reverses column indices

        # flip vertically
        else:
            output_image = newArray[::-1, :, :]  # reverses row indices

        return output_image

    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """

        # add your code here
        r, g, b = target_color
        height, width, _ = shape(foreground)  # gets dimensions of foreground

        for x in range(width):
            for y in range(height):
                r0 = foreground[y][x][0]
                g0 = foreground[y][x][1]
                b0 = foreground[y][x][2]

                # Euclidean distance algorithm
                distance = math.sqrt((r - r0) ** 2 + (g - g0) ** 2 + (b - b0) ** 2)
                if distance <= threshold:
                    # these pixels are replaced
                    foreground[y][x] = background[y][x]

        # Please do not change the structure
        return foreground  # Currently the input image is returned, please replace this with the color extracted image
