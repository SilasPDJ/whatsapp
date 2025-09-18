from time import sleep
import keyboard
import pyautogui as pg
from pyperclip import paste


sleep(5)
pg.click(pg.size().width / 2, pg.size().height / 2)
keyboard.press_and_release("ctrl+v")
sleep(2)
pg.press("enter")
sleep(2)
pg.press("enter")
sleep(2)

