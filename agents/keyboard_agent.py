import json
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
                #self.is_activated = not self.is_activated

        keyboard_listener = keyboard.Listener(on_press=on_keyboard_click)
        keyboard_listener.start()
        keyboard_listener.join()