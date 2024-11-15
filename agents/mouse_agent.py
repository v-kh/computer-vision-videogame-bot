from agents.settings_agent import SettingsAgent
from macros.QBZ_5_sens import QBZ5Sens
from pynput import mouse
import time


class MouseAgent:
    def __init__(self) -> None:
        self.capture_process = None
        self.is_activated = True

    def start_mouse_macros(self):
        def on_mouse_click(x, y, button, pressed):
            if button == mouse.Button.left:
                SettingsAgent.is_left_mouse_held = pressed
            if button == mouse.Button.right:
                SettingsAgent.is_right_mouse_held = pressed


        with (mouse.Listener(on_click=on_mouse_click) as mouse_listener):
            print("Listening for mouse events. Press Ctrl+C to stop.")

            try:
                while True:
                    if SettingsAgent.is_mouse_macros_activated:
                        if SettingsAgent.is_left_mouse_held and SettingsAgent.is_right_mouse_held:
                            QBZ5Sens.exec_macros(2.4)
                        if SettingsAgent.is_left_mouse_held and not SettingsAgent.is_right_mouse_held:
                            QBZ5Sens.exec_macros(1)
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("Stopped listening.")
                mouse_listener.stop()

        mouse_listener.join()
