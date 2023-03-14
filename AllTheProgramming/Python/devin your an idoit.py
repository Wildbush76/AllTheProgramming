import keyboard
import time
import mouse
file = open("countries","r")
countries = file.read().split("\n")

file.close()
time.sleep(3)
mouse.click("left")
time.sleep(0.1)
for yes in countries:
    keyboard.write(yes)
    time.sleep(0.01)
