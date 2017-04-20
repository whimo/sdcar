from driver_server import DriverServer
from calibrate import calibrate_camera
from stream import Stream
import cv2
import pygame
import sys


STREAM_URL = '192.168.0.100:8080/?action=stream'


def main():
    retval, camera_matrix, dict_coeffs, rvecs, tvecs = calibrate_camera()
    stream = Stream(STREAM_URL, camera_matrix, dict_coeffs)

    driver = DriverServer()
    driver.accept_connection()

    while True:
        stream.update()

        cv2.imshow('frame', stream.frame)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    driver.turn(1)

                if event.key == pygame.K_RIGHT:
                    driver.turn(2)

                if event.key == pygame.K_LEFT:
                    driver.turn(3)

                if event.key == pygame.K_DOWN:
                    driver.turn(4)

                if event.key == pygame.K_SPACE:
                    driver.turn(0)

                if event.key == pygame.K_q:
                    sys.exit()

        cv2.waitKey(4)


if __name__ == '__main__':
    main()
