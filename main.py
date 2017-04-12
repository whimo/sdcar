import cv2
import numpy as np

from calibrate import calibrate_camera
import processing
from stream import Stream


ROI_HEIGHT = 0.45
ROI_TOP = 0.15
ROI_BOTTOM = 0.8



def main():
    retval, camera_matrix, dict_coeffs, rvecs, tvecs = calibrate_camera()
    stream = Stream(url, camera_matrix, dict_coeffs)

    while True:
        stream.update()
        image = stream.frame
        shape = image.shape

        roi_edges = np.array([[
                            ((shape[1] * (1 - ROI_BOTTOM)) // 2, shape[0]),
                            ((shape[1] * (1 - ROI_TOP)) // 2, shape[0] - shape[0] * ROI_HEIGHT),
                            (shape[1] - (shape[1] * (1 - ROI_TOP)) // 2, shape[0] - shape[0] * ROI_HEIGHT),
                            (shape[1] - (shape[1] * (1 - ROI_BOTTOM)) // 2, shape[0])]],
                            dtype = np.int32)

        image = processing.color_filter     (image)
        image = processing.grayscale        (image)
        image = processing.region_of_intrest(image, roi_edges)
        image = processing.edges            (image)
        image = proessing.blur              (image)

        #here will go steering neural network prediction

        cv2.waitKey(1)



if __name__ == '__main__':
    main()
