import time
import pyautogui
from agents.settings_agent import SettingsAgent


class Sts6SensScope:
    @staticmethod
    def exec_macros():
        for x in range(4):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 15)
            time.sleep(0.022)

        for x in range(4):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 12)
            time.sleep(0.022)

        for x in range(46):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 7)
            time.sleep(0.022)

        for x in range(12):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 12)
            time.sleep(0.022)

        for x in range(38):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 10)
            time.sleep(0.025)

        for x in range(34):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 15)
            time.sleep(0.025)

        for x in range(22):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 13)
            time.sleep(0.025)

        for x in range(54):
            if not SettingsAgent.is_button_held:
                return

            pyautogui.moveRel(0, 15)
            time.sleep(0.025)
