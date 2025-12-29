import time
import cv2

class FPSCounter:
    def __init__(self):
        self.prev_time = 0
        self.curr_time = 0
        self.fps = 0

    def update(self):
        self.curr_time = time.time()
        delta = self.curr_time - self.prev_time
        if delta > 0:
            self.fps = 1 / delta
        self.prev_time = self.curr_time
        return self.fps

    def draw(self, image, pos=(20, 50), color=(255, 0, 0), scale=2, thickness=3):
        cv2.putText(
            image, 
            f"FPS: {int(self.fps)}", 
            pos, 
            cv2.FONT_HERSHEY_PLAIN, 
            scale, 
            color, 
            thickness
        )
