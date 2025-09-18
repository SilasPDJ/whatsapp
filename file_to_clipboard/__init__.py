import subprocess
from time import sleep
import keyboard
import pyautogui as pg


def copy_file_to_clipboard(file_path, wait=5):

    cmd = f'explorer /select,"{file_path}"'
    subprocess.Popen(cmd, shell=True)
    [(sleep(1), print(i)) for i in range(wait, 0, -1)]
    for i in range(2):
        keyboard.press_and_release("ctrl+c")


def paste_file():
    sleep(2)
    pg.click(pg.size().width / 2, pg.size().height / 2)
    sleep(.1)
    keyboard.press_and_release("ctrl+v")
    sleep(2)
    pg.press("enter")
    sleep(2)
    pg.press("enter")
    sleep(2)


if __name__ == "__main__":
    pass
