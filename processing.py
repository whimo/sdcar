import cv2
import numpy as np


WHITE_LOWER =  np.array([200, 200, 200])
WHITE_UPPER =  np.array([255, 255, 255])
YELLOW_LOWER = np.array([90,  100, 100])
YELLOW_UPPER = np.array([110, 255, 255])

GAUSSIAN_KERNEL_SIZE = 2

LOW_CANNY_THRESHOLD, HIGH_CANNY_THRESHOLD = 50, 150

RHO = 2
THETA = 1 * (np.pi / 180)
HOUGH_THRESHOLD = 15
MIN_LINE_LENGTH = 10
MAX_LINE_GAP = 20


class SteeringNeuralNetwork(object):
    '''
    Neural network for lane following
    '''

    def __init__(self):
        self.model = cv2.ANN_MLP()

        layers = np.int32([38400, 32, 4])
        self.model.create(layers)
        self.model.load('model.xml')


def undistort(image, camera_matrix, dict_coeffs):
    '''
    Returns an undistorted image
    (camera_matrix and dict_coeffs are provided by camera calibration)
    '''
    return cv2.undistort(image, camera_matrix, dict_coeffs)


def grayscale(image):
    '''
    Returns the image in gray scale
    '''
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def color_filter(image):
    '''
    Applies a color filter to recognize only white and yellow lines
    '''
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    white_filter =  cv2.inRange(image, WHITE_LOWER, WHITE_UPPER)
    yellow_filter = cv2.inRange(hsv_image, YELLOW_LOWER, YELLOW_UPPER)

    white_image =  cv2.bitwise_and(image, image, mask = white_filter)
    yellow_image = cv2.bitwise_and(image, image, mask = yellow_filter)

    return cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)


def blur(image):
    '''
    Applies a Gaussian blur to reduce noise
    '''
    return cv2.GaussianBlur(image, (GAUSSIAN_KERNEL_SIZE, GAUSSIAN_KERNEL_SIZE), 0)



def edges(image, low_threshold = LOW_CANNY_THRESHOLD, high_threshold = HIGH_CANNY_THRESHOLD):
    '''
    Performs a Canny transformation (contour detection) with the given image
    '''
    return cv2.Canny(image, low_threshold, high_threshold)


def region_of_intrest(image, edges):
    '''
    Erases part of grayscale image outside the region if intrest
    (specified by edges)
    '''
    mask = np.zeros_like(image)

    color = 255

    cv2.fillPoly(mask, edges, color)
    filtered = cv2.bitwise_and(image, mask)
    return filtered
