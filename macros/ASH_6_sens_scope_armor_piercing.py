import time
from ctypes import windll

from agents.settings_agent import SettingsAgent

class ASH6SensScopeArmorPiercing:
    @staticmethod
    def exec_macros():
        '''Mouse macros for Ash-12 gun is StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 5.
        StalCraft is in full windowed mode. For shooting with x2 scope with armor piercing bullets'''
        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 8, 0, 0)
            time.sleep(0.012)

        for x in range(8):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 7, 0, 0)
            time.sleep(0.012)

        for x in range(100):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 5, 0, 0)
            time.sleep(0.012)

        for x in range(21):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 7, 0, 0)
            time.sleep(0.012)

        for x in range(48):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 6, 0, 0)
            time.sleep(0.012)


