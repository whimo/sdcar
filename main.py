import cv2
import numpy as np

from calibrate import calibrate_camera
import processing


def main():
    retval, camera_matrix, dist_coeffs, rvecs, tvecs = calibrate_camera()

    image = cv2.imread('road1.jpg')
    #image = processing.undistort(image, camera_matrix, dist_coeffs)
    image = processing.edges(image)
    lines = processing.lines(image)

    cv2.imshow('edges', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
