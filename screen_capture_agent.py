import mss
import pyautogui
import cv2 as cv
import time
import numpy as np
from utils import hue_match_pct


class ScreenCaptureAgent:
    def __init__(self) -> None:
        self.img = None
        self.img_health = None
        self.img_health_HSV = None
        self.capture_process = None # Created process will be stored here. Get access to it form and outside of this class
        self.fps = None
        self.enable_cv_preview = True
        self.top_left = (3320, 1910)
        self.bottom_right = (3690, 1918)
        self.w, self.h = pyautogui.size() #current screen resolution
        self.monitor = { "top": 0, "left": 0, "width": self.w, "height": self.h } #monitor coordinates from (0,0)

    def capture_screen(self):
        fps_report_time = time.time()
        fps_report_delay = 5 # How often would we update fps
        n_frames = 1 # Start frame value. It will be incremented every while loop iteration.

        with mss.mss() as sct:
            while True:
                self.img = sct.grab(self.monitor) # ct is "screenshot". It takes a screenshot with monitor coordinates and size. Saves scr in memory.
                self.img = np.array(self.img) # Converts to array for opencv.
                self.img_health = self.img[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
                ]
                # self.img_health_HSV = cv.cvtColor(self.img_health, cv.COLOR_BGR2HSV)
                self.img_health_HSV = cv.cvtColor(self.img_health, cv.COLOR_BGR2RGB)

                if self.enable_cv_preview:
                    # Convert from rgb to bgr. Looks like for sct.grab(monitor). Apps in bgr, method in rgb.
                    small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5) # Takes image and scales it to *0.5
                    hp = cv.resize(self.img_health, (0, 0), fx=3, fy=3)

                    if self.fps is None:
                        fps_text = ""
                    else:
                        fps_text = f"FPS: {self.fps:.2f}"
                    cv.putText(small, fps_text, (25, 50), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1, cv.LINE_AA)
                    cv.putText(small, "Health: " + str(hue_match_pct(self.img_health_HSV, 0, 12)), (25, 100), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3, cv.LINE_AA)
                    cv.imshow('Computer vision', small) # Shows screenshot in small desktop window
                    cv.imshow("Health bar", hp)

                elapsed_time = time.time() - fps_report_time # Total time elapsed since we started program.

                if elapsed_time > fps_report_delay:
                    self.fps = n_frames / elapsed_time # FPS calculation.
                    print("FPS: " + str(self.fps))
                    n_frames = 0
                    fps_report_time = time.time()

                n_frames += 1
                cv.waitKey(1)  # Zero parameter waits for any key. It's like pause button. 1 is a 1 ms delay. Every 1 ms it check if any key is pressed.

# cv.destroyAllWindows() # Closes all windows