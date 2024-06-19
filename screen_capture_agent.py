import json
import mss
import pyautogui
import cv2 as cv
import numpy as np

from Models.rgb_model import RgbModel
from constants.default_values import DefaultValues
from utils.utils import rgb_match


class ScreenCaptureAgent:
    def __init__(self) -> None:
        f = open('appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.img = None
        self.img_health = None
        self.formatted_img_health = None
        self.capture_process = None
        self.enable_cv_preview = self.settings['isCvPreviewEnabled']
        self.top_left = (self.settings['monitoringAreaCoordinates']['topLeftX'], self.settings['monitoringAreaCoordinates']['topLeftY'])
        self.bottom_right = (self.settings['monitoringAreaCoordinates']['bottomRightX'], self.settings['monitoringAreaCoordinates']['bottomRightY'])
        self.w, self.h = pyautogui.size()
        self.monitor = {"top": DefaultValues.DEFAULT_VALUE, "left": DefaultValues.DEFAULT_VALUE, "width": self.w, "height": self.h}

    def capture_screen(self):
        with mss.mss() as sct:
            while True:
                self.img = sct.grab(self.monitor)  # ct is "screenshot". It takes a screenshot with monitor coordinates and size. Saves scr in memory.
                self.img = np.array(self.img)  # Converts screenshot to array for opencv.
                self.img_health = self.img[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
                ]

                self.formatted_img_health = cv.cvtColor(self.img_health, cv.COLOR_BGR2RGB) if self.settings['monitoringAreaCoordinates'] else cv.cvtColor(self.img_health, cv.COLOR_BGR2HSV)

                if self.enable_cv_preview:
                    # Convert from rgb to bgr. Looks like for sct.grab(monitor). Apps in bgr, method in rgb.
                    small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5) # Takes image and scales it to *0.5
                    hp = cv.resize(self.img_health, (0, 0), fx=3, fy=3)
                    rgb_model = RgbModel(114, 145, 30, 57, 27, 57)

                    cv.putText(small, "Health: " + str(rgb_match(self.formatted_img_health, rgb_model)), (25, 100), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3, cv.LINE_AA)
                    cv.imshow('Computer vision', small) # Shows screenshot in small desktop window
                    cv.imshow("Health bar", hp)

                cv.waitKey(1)  # Zero parameter waits for any key. It's like pause button. 1 is a 1 ms delay. Every 1 ms it check if any key is pressed.

# cv.destroyAllWindows() # Closes all .imshow() windows