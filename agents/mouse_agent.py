from agents.settings_agent import SettingsAgent
from pynput import mouse
import time

class MouseAgent:
    def __init__(self) -> None:
        self.capture_process = None
        self.is_activated = True
        self.is_button_held = False

    def start_mouse_macros(self):
        def on_mouse_click(x, y, button, pressed):
            if button == mouse.Button.right:
                self.is_button_held = pressed

        with mouse.Listener(on_click=on_mouse_click) as mouse_listener:
            #pyautogui.moveRel(1, 10)
            print("Listening for mouse events. Press Ctrl+C to stop.")

            try:
                while True:
                    if SettingsAgent.is_mouse_macros_activated and self.is_button_held:
                        print("Right mouse button is being held down.")
                    time.sleep(0.1)  # Check every 100 ms
            except KeyboardInterrupt:
                print("Stopped listening.")
                mouse_listener.stop()

        mouse_listener.join()
