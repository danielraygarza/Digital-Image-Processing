from .interpolation import interpolation
from dip import *
import math

class Distort:
    def __init__(self):
        pass

    def distortion(self, image, k):
        """Applies distortion to the image
                image: input image
                k: distortion Parameter
                return the distorted image"""
        
        # get dimensions of input image
        height = image.shape[0]
        width = image.shape[1]

        # center of image
        cx = width / 2
        cy = height / 2 

        # initialize empty array for new image
        distorted_image = zeros(shape = image.shape, dtype = image.dtype)

        # iterate through each pixel in image
        for i in range(width):
            for j in range(height):
                
                # position w respect to center
                ic = i - cx
                jc = j - cy

                # pythagorean theorem to get distance from center
                r = math.sqrt(ic ** 2 + jc ** 2)
                
                # apply distortion formula
                icd = ic / (1 + (k*r))
                jcd = jc / (1 + (k*r))

                # apply change in coordinate system 
                id = round(icd + cx)
                jd = round(jcd + cy)

                # copy pixel values to new disorted image
                if 0 <= id < width and 0 <= jd < height:
                    distorted_image[jd, id] = image[j, i]

        return distorted_image


    def correction_naive(self, distorted_image, k):
        """Applies correction to a distorted image by applying the inverse of the distortion function
        image: the input image
        k: distortion parameter
        return the corrected image"""

        # get dimensions of input image
        height = distorted_image.shape[0]
        width = distorted_image.shape[1]

        # center of image
        cx = width / 2
        cy = height / 2 

        # initialize empty array for new image
        corrected_image = zeros(shape = distorted_image.shape, dtype = distorted_image.dtype)

        # iterate through each pixel in the distorted image
        for i in range(width):
            for j in range(height):
                
                # position w respect to center
                ic = i - cx
                jc = j - cy

                # pythagorean theorem to get distance from center
                r = math.sqrt(ic ** 2 + jc ** 2)
                
                # apply inverse distortion formula
                icd = ic * (1 + (k*r))
                jcd = jc * (1 + (k*r))

                # apply change in coordinate system 
                id = round(icd + cx)
                jd = round(jcd + cy)

                # copy pixel values to new corrected image
                if 0 <= id < width and 0 <= jd < height:
                    corrected_image[jd, id] = distorted_image[j, i]

        return corrected_image

    def correction(self, distorted_image, k, interpolation_type):
        """Applies correction to a distorted image and performs interpolation
                image: the input image
                k: distortion parameter
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the corrected image"""
        
        # get dimensions of input image
        height = distorted_image.shape[0]
        width = distorted_image.shape[1]

        # center of image
        cx = width / 2
        cy = height / 2 

        # initialize empty array for new image
        corrected_image = zeros(shape = distorted_image.shape, dtype = distorted_image.dtype)

        # iterate through each pixel in the distorted image
        for i in range(width):
            for j in range(height):
                
                # position w respect to center
                ic = i - cx
                jc = j - cy

                # pythagorean theorem to get distance from center
                r = math.sqrt(ic ** 2 + jc ** 2)
                
                # apply distortion formula
                icd = ic / (1 + (k*r))
                jcd = jc / (1 + (k*r))

                # apply change in coordinate system 
                id = round(icd + cx)
                jd = round(jcd + cy)

                if interpolation_type == 'nearest_neighbor':
                    # copy pixels to nearest neighbor
                    inn = round(id)
                    jnn = round(jd)
                    corrected_image[j, i] = distorted_image[jnn, inn]

                elif interpolation_type == 'bilinear':
                    # calculate bilinear interpolated value
                    interpolated_value = interpolation().bilinear_interpolation(distorted_image, (id, jd))

                    # copy pixel values to new corrected image
                    corrected_image[round(j), round(i)] = interpolated_value

        return corrected_image
