import json

from playsound import playsound # exactly pip install playsound==1.2.2
from pynput import keyboard

from agents.settings_agent import SettingsAgent

class KeyboardAgent:
    def __init__(self):
        f = open('./appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.activate_macros_key_cap = f'{self.settings['activateMacrosKeyCap']}'
        self.capture_process = None

    def start_keyboard_listening(self):
        def on_keyboard_click(key):
            #if key.char and key.char == self.activate_macros_key_cap:
            try:
                if key.char and key.char == self.activate_macros_key_cap:
                    if SettingsAgent.is_mouse_macros_activated:
                        SettingsAgent.is_mouse_macros_activated = False
                        playsound('./sounds/deactivated.mp3')
                    else:
                        SettingsAgent.is_mouse_macros_activated = True
                        playsound('./sounds/activated.mp3')
            except Exception as e: None

        keyboard_listener = keyboard.Listener(on_press=on_keyboard_click)
        keyboard_listener.start()
        keyboard_listener.join()