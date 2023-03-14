import pygame
import pyautogui
import math
pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(len(joysticks))

running = True

SPEED = 10
SPEECURVE = 2
FRAMERATE = 50



clock = pygame.time.Clock()
while running:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if joysticks[0].get_button(0) == True:
                pyautogui.mouseDown()
            else:
                pyautogui.mouseUp()
            if joysticks[0].get_button(1) == True:
                pyautogui.rightClick()
                
       # elif event.type == pygame.JOYAXISMOTION:
    x = joysticks[0].get_axis(0)
    y = joysticks[0].get_axis(1)
            #print(f" x {x} y {y}")
    pyautogui.move(math.copysign(math.pow(x*SPEED,SPEECURVE),x) , math.copysign(math.pow(y*SPEED,SPEECURVE),y),1/FRAMERATE)


pygame.quit()
pygame.joystick.quit()
