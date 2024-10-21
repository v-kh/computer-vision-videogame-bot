import json
from nava import play
from playsound import playsound

from agents.settings_agent import SettingsAgent
from pynput import keyboard

from pynput.keyboard import KeyCode


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
            if key == keyboard.Key.up:
                if SettingsAgent.is_mouse_macros_activated:
                    SettingsAgent.is_mouse_macros_activated = False
                    playsound('./sounds/deactivated.mp3')
                else:
                    SettingsAgent.is_mouse_macros_activated = True
                    playsound('./sounds/activated.mp3')

        keyboard_listener = keyboard.Listener(on_press=on_keyboard_click)
        keyboard_listener.start()
        keyboard_listener.join()