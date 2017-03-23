import cv2
import numpy as np

from calibrate import calibrate_camera


def main():
    cameraMatrix = calibrate_camera()

    return cameraMatrix


if __name__ == '__main__':
    main()
