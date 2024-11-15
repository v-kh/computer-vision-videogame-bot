import time
from ctypes import windll

from agents.settings_agent import SettingsAgent


class QBZ5SensHeap:
    @staticmethod
    def exec_macros():
        '''Mouse macros for QBZ gun is StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 5.
        StalCraft is in full windowed mode. For shooting without scope'''
        for x in range(10):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 5, 0, 0)
            time.sleep(0.022)

        for x in range(32):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 4, 0, 0)
            time.sleep(0.022)

        for x in range(30):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 6, 0, 0)
            time.sleep(0.022)

        for x in range(20):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 5, 0, 0)
            time.sleep(0.022)

        for x in range(50):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 7, 0, 0)
            time.sleep(0.022)
