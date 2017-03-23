import cv2
import numpy as np
import glob


def calibrate_camera(chessboard_path = 'chessboard/*.jpg'):
    '''
    Function for camera calibration
    10x7 chessboard images captured with the camera that you want to calibrate
    should be placed to the chessboard folder or anywhere
    (in that case the path should be specified)

    Returns the output of OpenCV calibrateCamera() function
    '''
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    object_point = np.zeros((6 * 9, 3), np.float32)
    object_point[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    object_points = []
    image_points = []
    height, width = 0, 0

    images = glob.glob(chessboard_path)

    for file_name in images:
        image = cv2.imread(file_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape[:2]

        # find chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

        # add object points, image points
        if ret:
            object_points.append(object_point)
            cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            image_points.append(corners)

    return cv2.calibrateCamera(object_points, image_points, (width, height), None, None)
