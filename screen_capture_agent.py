import json
import time
import mss
import pyautogui
import cv2 as cv
import numpy as np
import winsound
from pynput import mouse

from Models.rgb_model import RgbModel
from constants.default_values import DefaultValues
from utils.utils import rgb_match

class ScreenCaptureAgent:
    def __init__(self) -> None:
        f = open('appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.is_button_held = False

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
        self.r_low = self.settings['monitoringAreaColorRgb']['rLow']
        self.r_high = self.settings['monitoringAreaColorRgb']['rHigh']
        self.g_low = self.settings['monitoringAreaColorRgb']['gLow']
        self.g_high = self.settings['monitoringAreaColorRgb']['gHigh']
        self.b_low = self.settings['monitoringAreaColorRgb']['bLow']
        self.b_high = self.settings['monitoringAreaColorRgb']['bHigh']
        self.trigger_value_low = self.settings['triggerValueLow']
        self.trigger_value_high = self.settings['triggerValueHigh']
        self.trigger_interval = self.settings['triggerInterval']
        self.target_key_cap = self.settings['targetKeyCap']
        self.w, self.h = pyautogui.size()
        self.monitor_dimensions = {"top": DefaultValues.DEFAULT_VALUE, "left": DefaultValues.DEFAULT_VALUE, "width": self.w, "height": self.h}

    def capture_screen(self):
        def on_click(x, y, button, pressed):
            if button == mouse.Button.right:  # Check for the left mouse button
                self.is_button_held = pressed
                if pressed:
                    print("Right mouse button pressed.")
                else:
                    print("Right mouse button released.")

        # Set up the listener
        with mouse.Listener(on_click=on_click) as listener:
            print("Listening for mouse events. Press Ctrl+C to stop.")
            try:
                while True:
                    if self.is_button_held:
                        print("Right mouse button is being held down.")
                    time.sleep(0.1)  # Check every 100 ms
            except KeyboardInterrupt:
                print("Stopped listening.")
                listener.stop()

        # sct is "screenshot". It takes a screenshot with monitor coordinates and size. Saves sct in memory.
        with mss.mss() as sct:
            while True:
                self.full_monitor = sct.grab(self.monitor_dimensions)
                self.full_monitor = np.array(self.full_monitor)  # Converts screenshot to array for opencv.
                self.target_area = self.full_monitor[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
               ]

                # DEPRECATED: HSV color model will probably be deleted
                # self.formatted_target_area = cv.cvtColor(self.target_area, cv.COLOR_BGR2RGB) if self.is_rgb_mode_selected else cv.cvtColor(self.target_area, cv.COLOR_BGR2HSV)
                self.formatted_target_area = cv.cvtColor(self.target_area, cv.COLOR_BGR2RGB)
                rgb_model = RgbModel(self.r_low, self.r_high, self.g_low, self.g_high, self.b_low, self.b_high)
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
                    hp_monitor = cv.resize(self.target_area, (0, 0), fx=2, fy=10)
                    health_bar_window_name = "Health bar"

                    cv.putText(hp_monitor, "Health: " + str(hp), (25, 45), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3, cv.LINE_AA)
                    cv.putText(hp_monitor, "Power: ON", (400, 45), cv.FONT_HERSHEY_PLAIN, 3, (250, 160, 120), 3, cv.LINE_4) # color param is in BGR
                    #cv.imshow(main_monitor_window_name, main_monitor) # Shows screenshot in small desktop window
                    cv.imshow(health_bar_window_name, hp_monitor)
                    cv.setWindowProperty(health_bar_window_name, cv.WND_PROP_TOPMOST, 1)

                cv.waitKey(self.monitoring_threshold_ms)  # Zero parameter waits for any key. It's like pause button. 1 is a 1 ms delay. Every 1 ms it check if any key is pressed.

# cv.destroyAllWindows() # Closes all .imshow() windows