import cv2

class Camera:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)

    def get_frame(self):
        """
        return a frame from the camera
        """
        success, img = self.cap.read()
        if success:
            return img
        return None

    def save_frame(self, output_path):
        filename = output_path
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
