import time
from ctypes import windll
from agents.settings_agent import SettingsAgent


class Sts5SensHeap:
    @staticmethod
    def exec_macros(scope_multiplier):
        '''Mouse macros for STS gun is StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 5.
        StalCraft is in full windowed mode. For shooting without scope'''
        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(10 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(8 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(23):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(5 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(8):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(6 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(19):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(7 * scope_multiplier), 0, 0)
            time.sleep(0.025)

        for x in range(17):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(9 * scope_multiplier), 0, 0)
            time.sleep(0.025)

        for x in range(11):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(9 * scope_multiplier), 0, 0)
            time.sleep(0.025)

        for x in range(12):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(9 * scope_multiplier), 0, 0)
            time.sleep(0.025)

        for x in range(15):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(8 * scope_multiplier), 0, 0)
            time.sleep(0.025)

        #insound.Beep(frequency=2500, duration=10)
