import time
from ctypes import windll
from agents.settings_agent import SettingsAgent


class Mg35Sens:
    @staticmethod
    def exec_macros(scope_multiplier):
        '''Mouse macros for MG3 machinegun is StalCraft video game.
        For win 3840x2160 with 150% percent view, mouse sensitivity 5.
        StalCraft is in full windowed mode.'''
        for x in range(4):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(13 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(20):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(9 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(100):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(11 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        for x in range(50):
            if not SettingsAgent.is_left_mouse_held:
                return

            windll.user32.mouse_event(1, 0, round(10 * scope_multiplier), 0, 0)
            time.sleep(0.022)

        #insound.Beep(frequency=2500, duration=10)
