import time
from ctypes import windll
from agents.settings_agent import SettingsAgent


class Sts6SensScope:
    @staticmethod
    def exec_macros():
        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 20, 0, 0)
            time.sleep(0.022)

        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 14, 0, 0)
            time.sleep(0.022)

        for x in range(23):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 9, 0, 0)
            time.sleep(0.022)

        for x in range(8):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 10, 0, 0)
            time.sleep(0.022)

        for x in range(19):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 12, 0, 0)
            time.sleep(0.025)

        for x in range(17):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 14, 0, 0)
            time.sleep(0.025)

        for x in range(11):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 16, 0, 0)
            time.sleep(0.025)

        for x in range(12):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 16, 0, 0)
            time.sleep(0.025)

        for x in range(15):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 15, 0, 0)
            time.sleep(0.025)

        #insound.Beep(frequency=2500, duration=10)
