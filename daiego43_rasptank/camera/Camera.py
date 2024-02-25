import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, img = self.cap.read()
        if success:
            return img
        return None

    def save_frame(self, filename):
        filename = "/tmp/pycharm_project_514/daiego43_rasptank/camera/" + filename
        print("Trying to save frame... ", end="")
        while True:
            frame = self.get_frame()
            if frame is not None:
                cv2.imwrite(filename, frame)
                break

        print("Foto guardada en " + filename)


if __name__ == '__main__':
    camara = Camera()
    camara.save_frame("test.jpg")
