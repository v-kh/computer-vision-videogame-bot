from agents.settings_agent import SettingsAgent
from macros.sts_6_sens_scope import Sts6SensScope
from pynput import mouse
import time


class MouseAgent:
    def __init__(self) -> None:
        self.capture_process = None
        self.is_activated = True

    def start_mouse_macros(self):
        def on_mouse_click(x, y, button, pressed):
            if button == mouse.Button.left:
                SettingsAgent.is_button_held = pressed

        with mouse.Listener(on_click=on_mouse_click) as mouse_listener:
            print("Listening for mouse events. Press Ctrl+C to stop.")

            try:
                while True:
                    if SettingsAgent.is_mouse_macros_activated and SettingsAgent.is_button_held:
                        Sts6SensScope.exec_macros()
                    time.sleep(0.1)  # Check every 100 ms
            except KeyboardInterrupt:
                print("Stopped listening.")
                mouse_listener.stop()

        mouse_listener.join()
