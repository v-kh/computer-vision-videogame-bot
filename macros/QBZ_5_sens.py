import math
import time
from ctypes import windll
from agents.settings_agent import SettingsAgent


class QBZ5Sens:
    @staticmethod
    def exec_macros(scope_multiplier):
        '''Mouse macros for QBZ gun in StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 6.
        StalCraft is in full windowed mode.'''
        for x in range(2):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(6 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(8):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(5 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(32):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(4 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(30):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(5 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(70):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(6.5 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        #winsound.Beep(frequency=2500, duration=10)
