# video seria: https://www.youtube.com/watch?v=giuzj-EPOVc&t=138s
import mss
import pyautogui
import cv2 as cv
import numpy as np
import time
import multiprocessing


class ScreenCaptureAgent:
    def __init__(self) -> None:
        self.img = None
        self.img_health = None
        self.img_health_HSV = None
        self.capture_process = None # Created process will be stored here. Get access to it form and outside of this class
        self.fps = None
        self.enable_cv_preview = True
        self.top_left = (3314, 1910)
        self.bottom_right = (3697, 1918)
        self.w, self.h = pyautogui.size() #current screen resolution
        self.monitor = { "top": 0, "left": 0, "width": self.w, "height": self.h } #monitor coordinates from (0,0)

    def capture_screen(self):
        fps_report_time = time.time()
        fps_report_delay = 5 # How often would we update fps
        n_frames = 1 # Start frame value. It will be incremented every while loop iteration.

        with mss.mss() as sct:
            while True:
                self.img = sct.grab(self.monitor) # ct is "screenshot". It takes a screenshot with monitor coordinates and size. Saves scr in memory.
                self.img = np.array(self.img) # Converts to array for opencv.
                self.img_health = self.img[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
                ]
                self.img_health_HSV = cv.cvtColor(self.img_health, cv.COLOR_BGR2HSV)

                if self.enable_cv_preview:
                    # Convert from rgb to bgr. Looks like for sct.grab(monitor). Apps in bgr, method in rgb.
                    small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5) # Takes image and scales it to *0.5

                    if self.fps is None:
                        fps_text = ""
                    else:
                        fps_text = f"FPS: {self.fps:.2f}"
                    cv.putText(small, fps_text, (25, 50), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1, cv.LINE_AA)
                    cv.putText(small, "Health: " + str(hue_match_pct(self.img_health_HSV, 0, 10)), (25, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv.LINE_AA)
                    cv.imshow('Computer vision', small) # Shows screenshot in small desktop window
                    cv.imshow("Health bar", self.img_health)

                elapsed_time = time.time() - fps_report_time # Total time elapsed since we started program.

                if elapsed_time > fps_report_delay:
                    self.fps = n_frames / elapsed_time # FPS calculation.
                    print("FPS: " + str(self.fps))
                    n_frames = 0
                    fps_report_time = time.time()

                n_frames += 1
                cv.waitKey(1)  # Zero parameter waits for any key. It's like pause button. 1 is a 1 ms delay. Every 1 ms it check if any key is pressed.

# cv.destroyAllWindows() # Closes all windows


class bcolors:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def convert_hue(hue):
    ratio = 361 / 180
    return np.round(hue / ratio, 2)

def hue_match_pct(img, hue_low, hue_high):
    match_pixels = 0
    no_match_pixels = 0
    for pixel in img:
        for h, s, v in pixel:
            if convert_hue(hue_low) <= h <= convert_hue(hue_high): # убрать convert_hue
                match_pixels += 1
            else:
                no_match_pixels += 1

    total_pixels = match_pixels + no_match_pixels
    return np.round(match_pixels / total_pixels, 2) * 100

def print_menu():
    print(f'{bcolors.CYAN}Command menu{bcolors.ENDC}')
    print(f'\t{bcolors.GREEN}r - run{bcolors.ENDC} \tStart screen capture')
    print(f'\t{bcolors.RED}s - stop{bcolors.ENDC} \tStop screen capture')
    print(f'\tq - quit \tQuit the program')


def f():
    print(1)


if __name__ == "__main__":
    screen_agent = ScreenCaptureAgent()

    while True:
        print_menu()
        user_input = input().strip().lower()
        if user_input == 'quit' or user_input == 'q':
            if screen_agent.capture_process is not None:
                screen_agent.capture_process.terminate()
            break
        elif user_input == 'run' or user_input == 'r':
            if screen_agent.capture_process is not None:
                print(f'{bcolors.YELLOW}WARNING:{bcolors.ENDC} Capture process is running.')
                continue

            screen_agent.capture_process = multiprocessing.Process(
                target=screen_agent.capture_screen,
                args=(),
                name="screen capture process"
            )
            screen_agent.capture_process.start() # не работает 28:30
            screen_agent.capture_process.join(1)
        elif user_input == 'stop' or user_input == 's':
            if screen_agent.capture_process is None:
                print(f'{bcolors.YELLOW}WARNING:{bcolors.ENDC} Capture process is not running.')
                continue

            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
        else:
            print(f'{bcolors.RED}ERROR:{bcolors.ENDC} Invalid selection')

print("Done.")
