import json
import time
import mss
import pyautogui
import cv2 as cv
import numpy as np
import winsound

from Models.rgb_model import RgbModel
from constants.default_values import DefaultValues
from utils.utils import rgb_match


class ScreenCaptureAgent:
    def __init__(self) -> None:
        f = open('appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.time = time.time()
        self.full_monitor = None
        self.target_area = None
        self.formatted_target_area = None
        self.capture_process = None
        self.isDebugMode = self.settings['isDebugMode']
        self.monitoring_threshold_ms = self.settings['monitoringThresholdMs']
        self.is_cv_preview_enabled = self.settings['isCvPreviewEnabled']
        self.top_left = (self.settings['monitoringAreaCoordinates']['topLeftX'], self.settings['monitoringAreaCoordinates']['topLeftY'])
        self.bottom_right = (self.settings['monitoringAreaCoordinates']['bottomRightX'], self.settings['monitoringAreaCoordinates']['bottomRightY'])
        self.is_rgb_mode_selected = self.settings['isRgbModeSelected']
        self.trigger_value_low = self.settings['triggerValueLow']
        self.trigger_value_high = self.settings['triggerValueHigh']
        self.trigger_interval = self.settings['triggerInterval']
        self.target_key_cap = self.settings['targetKeyCap']
        self.w, self.h = pyautogui.size()
        self.monitor_dimensions = {"top": DefaultValues.DEFAULT_VALUE, "left": DefaultValues.DEFAULT_VALUE, "width": self.w, "height": self.h}

    def capture_screen(self):
        # sct is "screenshot". It takes a screenshot with monitor coordinates and size. Saves sct in memory.
        with mss.mss() as sct:
            while True:
                self.full_monitor = sct.grab(self.monitor_dimensions)
                self.full_monitor = np.array(self.full_monitor)  # Converts screenshot to array for opencv.
                self.target_area = self.full_monitor[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
               ]

                self.formatted_target_area = cv.cvtColor(self.target_area, cv.COLOR_BGR2RGB) if self.is_rgb_mode_selected else cv.cvtColor(self.target_area, cv.COLOR_BGR2HSV)
                rgb_model = RgbModel(105, 145, 23, 57, 23, 57)
                hp = rgb_match(self.formatted_target_area, rgb_model)
                current_time = time.time()
                time_elapsed = current_time - self.time

                if self.trigger_value_low < hp < self.trigger_value_high and self.isDebugMode:
                    winsound.Beep(frequency = 2500, duration = 10)
                    print("Event triggered")

                if self.trigger_value_low < hp < self.trigger_value_high and time_elapsed > self.trigger_interval and not self.isDebugMode:
                    self.time = time.time()
                    pyautogui.press(self.target_key_cap)

                if self.is_cv_preview_enabled:
                    # Convert from rgb to bgr. Looks like for sct.grab(monitor). Apps in bgr, method in rgb.
                    #main_monitor = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5) # Takes image and scales it to *0.5
                    # main_monitor_window_name = "Computer vision"
                    hp_monitor = cv.resize(self.target_area, (0, 0), fx=3, fy=30)
                    health_bar_window_name = "Health bar"

                    cv.putText(hp_monitor, "Health: " + str(hp), (25, 100), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3, cv.LINE_AA)
                    cv.putText(hp_monitor, "Power: ON", (620, 100), cv.FONT_HERSHEY_PLAIN, 5, (250, 160, 120), 3, cv.LINE_4) # color param is in BGR
                    #cv.imshow(main_monitor_window_name, main_monitor) # Shows screenshot in small desktop window
                    cv.imshow(health_bar_window_name, hp_monitor)
                    cv.setWindowProperty(health_bar_window_name, cv.WND_PROP_TOPMOST, 1)

                cv.waitKey(self.monitoring_threshold_ms)  # Zero parameter waits for any key. It's like pause button. 1 is a 1 ms delay. Every 1 ms it check if any key is pressed.

# cv.destroyAllWindows() # Closes all .imshow() windows