import random
import pyautogui as pg
import time
words=['Dog','Cat','Bull']
time.sleep(5)
for i in range(2):
    a=random.choice(words)
    pg.write("It is a "+a)
    pg.press('enter')