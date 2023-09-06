import random

import pyautogui as pg

import time

animal = ("paglol","cute monkey","mottli")

time.sleep(5)

for i in range(10):
    a = random.choice(animal)
    pg.write("you are a "+a)
    pg.press('enter')
