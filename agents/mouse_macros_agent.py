from pynput import mouse
import pyautogui
import time

class MouseMacrosAgent:
    def __init__(self) -> None:
        self.is_button_held = False
        self.capture_process = None

    def start_mouse_macros(self):
        def on_click(x, y, button, pressed):
            if button == mouse.Button.right:  # Check for the left mouse button
                self.is_button_held = pressed
                if pressed:
                    print("Right mouse button pressed.")
                else:
                    print("Right mouse button released.")

        with mouse.Listener(on_click=on_click) as listener:
            #pyautogui.moveRel(1, 10)
            print("Listening for mouse events. Press Ctrl+C to stop.")
            try:
                while True:
                    if self.is_button_held:
                        print("Right mouse button is being held down.")
                    time.sleep(0.1)  # Check every 100 ms
            except KeyboardInterrupt:
                print("Stopped listening.")
                listener.stop()

        listener.join()