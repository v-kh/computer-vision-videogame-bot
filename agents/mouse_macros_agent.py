import json
from pynput import mouse, keyboard
import time
import winsound

class MouseMacrosAgent:
    def __init__(self) -> None:
        f = open('./appsettings.json')
        self.settings = json.load(f)
        f.close()

        self.activate_macros_key_cap = self.settings['activateMacrosKeyCap']

        self.capture_process = None
        self.is_activated = True
        self.is_button_held = False

    def start_mouse_macros(self):
        def on_keyboard_click(key):
            if key == keyboard.Key.up:
                winsound.Beep(frequency=2500, duration=10)
                self.is_activated = not self.is_activated

        keyboard_listener = keyboard.Listener(on_press=on_keyboard_click) # Если привести к вид как у mouse_listener, он как-то начинает работать.

        def on_mouse_click(x, y, button, pressed):
            if button == mouse.Button.right:
                self.is_button_held = pressed
                if self.is_button_held:
                    print("Right mouse button pressed.")
                else:
                    print("Right mouse button released.")

        with mouse.Listener(on_click=on_mouse_click) as mouse_listener:
            #pyautogui.moveRel(1, 10)
            print("Listening for mouse events. Press Ctrl+C to stop.")

            try:
                while True:
                    if self.is_activated and self.is_button_held:
                        print("Right mouse button is being held down.")
                    time.sleep(0.1)  # Check every 100 ms
            except KeyboardInterrupt:
                print("Stopped listening.")
                mouse_listener.stop()

        keyboard_listener.join()
        mouse_listener.join()
