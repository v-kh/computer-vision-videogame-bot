import multiprocessing

from constants.colors import Colors
from constants.user_inputs import UserInputs
from agents.screen_capture_agent import ScreenCaptureAgent
from agents.mouse_macros_agent import MouseMacrosAgent


def print_menu():
    print(f'{Colors.CYAN}Command menu{Colors.DEFAULT}')
    print(f'\t{Colors.GREEN}r - run{Colors.DEFAULT} \tStart screen capture')
    print(f'\t{Colors.RED}s - stop{Colors.DEFAULT} \tStop screen capture')
    print(f'\tq - quit \tQuit the program')


if __name__ == "__main__":
    screen_agent = ScreenCaptureAgent()
    mouse_macros_agent = MouseMacrosAgent()

    while True:
        print_menu()

        user_input = input().strip().lower()

        if user_input == UserInputs.QUIT_COMMAND or user_input == UserInputs.QUIT_KEY:
            if screen_agent.capture_process is not None and mouse_macros_agent.capture_process is not None:
                screen_agent.capture_process.terminate()

            break
        elif user_input == UserInputs.RUN_COMMAND or user_input == UserInputs.RUN_KEY:
            if screen_agent.capture_process is not None and mouse_macros_agent.capture_process is not None:
                print(f'{Colors.YELLOW}WARNING:{Colors.DEFAULT} Processes are running.')
                continue

            mouse_macros_agent.capture_process = multiprocessing.Process(
                target=mouse_macros_agent.start_mouse_macros,
                args=(),
                name="mouse macros process"
            )

            screen_agent.capture_process = multiprocessing.Process(
                target=screen_agent.capture_screen,
                args=(),
                name="screen capture process"
            )

            screen_agent.capture_process.start()
            mouse_macros_agent.capture_process.start()
            mouse_macros_agent.capture_process.join()
            screen_agent.capture_process.join()

        elif user_input == UserInputs.STOP_COMMAND or user_input == UserInputs.STOP_KEY:
            if screen_agent.capture_process is None and mouse_macros_agent.capture_process is None:
                print(f'{Colors.YELLOW}WARNING:{Colors.DEFAULT} Processes are not running.')
                continue

            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
            mouse_macros_agent.capture_process.terminate()
            mouse_macros_agent.capture_process = None
        else:
            print(f'{Colors.RED}ERROR:{Colors.DEFAULT} Invalid selection')

print("Done.")
