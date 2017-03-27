import cv2
import urllib
import numpy as np


class Stream(object):
    def __init__(self, url, camera_matrix, dict_coeffs):
        self.stream = urllib.urlopen(url)
        self.camera_matrix = camera_matrix
        self.dict_coeffs = dict_coeffs
        self.bytes = ''
        self.frame = None

    def update(self):
        self.bytes += self.stream.read(1024)
        start = self.bytes.find('\xff\xd8')
        end =   self.bytes.find('\xff\xd9')

        if start != -1 and end != -1:
            jpg = self.bytes[start:end + 2]
            self.bytes = self.bytes[end + 2:]
            self.frame = cv2.undistort(cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), cv2.CV_LOAD_IMAGE_COLOR),
                                       self.camera_matrix,
                                       self.dict_coeffs)
