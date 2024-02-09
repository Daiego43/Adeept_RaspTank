import cv2
import time


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, img = self.cap.read()
        if not success:
            return None
        return img


if __name__ == '__main__':
    camara = Camera()
    frame = camara.get_frame()
    cv2.imwrite('frame.jpg', frame)
