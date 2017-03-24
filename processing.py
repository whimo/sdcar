import cv2
import numpy as np

LOW_THRESHOLD, HIGH_THRESHOLD = 50, 150

RHO = 2
THETA = 1 * (np.pi / 180)
HOUGH_THRESHOLD = 15
MIN_LINE_LENGTH = 10
MAX_LINE_GAP = 20


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


def edges(image, low_threshold = LOW_THRESHOLD, high_threshold = HIGH_THRESHOLD):
    '''
    Performs a Canny transformation (contour detection) with the given image
    '''
    return cv2.Canny(image, low_threshold, high_threshold)
