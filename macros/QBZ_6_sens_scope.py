import time
from ctypes import windll
from agents.settings_agent import SettingsAgent


class QBZ5SensScope:
    @staticmethod
    def exec_macros():
        '''Mouse macros for STS gun in StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 6.
        StalCraft is in full windowed mode. For shooting in 2x scope.'''
        for x in range(10):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 10, 0, 0)
            time.sleep(0.022)

        for x in range(32):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 8, 0, 0)
            time.sleep(0.022)

        for x in range(30):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 10, 0, 0)
            time.sleep(0.022)

        for x in range(70):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, 13, 0, 0)
            time.sleep(0.022)

        #winsound.Beep(frequency=2500, duration=10)
