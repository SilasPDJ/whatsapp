from f8 import WaitPressF8
import pyautogui as pg
import clipboard


def exec():
    pos = pg.position()

    clipboard.copy(f"{pos.x}, {pos.y}")


WaitPressF8(exec, use_gui=False)
