import multiprocessing

from constants.colors import Colors
from screen_capture_agent import ScreenCaptureAgent


def print_menu():
    print(f'{Colors.CYAN}Command menu{Colors.DEFAULT}')
    print(f'\t{Colors.GREEN}r - run{Colors.DEFAULT} \tStart screen capture')
    print(f'\t{Colors.RED}s - stop{Colors.DEFAULT} \tStop screen capture')
    print(f'\tq - quit \tQuit the program')


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
                print(f'{Colors.YELLOW}WARNING:{Colors.DEFAULT} Capture process is running.')
                continue

            screen_agent.capture_process = multiprocessing.Process(
                target=screen_agent.capture_screen,
                args=(),
                name="screen capture process"
            )
            screen_agent.capture_process.start()
            screen_agent.capture_process.join(1)
        elif user_input == 'stop' or user_input == 's':
            if screen_agent.capture_process is None:
                print(f'{Colors.YELLOW}WARNING:{Colors.DEFAULT} Capture process is not running.')
                continue

            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
        else:
            print(f'{Colors.RED}ERROR:{Colors.DEFAULT} Invalid selection')

print("Done.")
