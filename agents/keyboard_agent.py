import json

from agents.settings_agent import SettingsAgent
from pynput import keyboard
import winsound

class KeyboardAgent:
    def __init__(self):
        f = open('./appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.activate_macros_key_cap = f'{self.settings['activateMacrosKeyCap']}'
        self.capture_process = None

    def start_keyboard_listening(self):
        def on_keyboard_click(key):
            if key.char == self.activate_macros_key_cap:
                winsound.Beep(frequency=2500, duration=10)
                SettingsAgent.is_mouse_macros_activated = not SettingsAgent.is_mouse_macros_activated

        keyboard_listener = keyboard.Listener(on_press=on_keyboard_click)
        keyboard_listener.start()
        keyboard_listener.join()