from PIL import ImageGrab
import pain
import mouse
import time
box = [658,213,1258,813]
def getScreen():
    ScreenShot = ImageGrab.grab(bbox = tuple(box))
    ScreenShot.save("test.png")
    pixels = ScreenShot.getdata()
    points = []
    for y in range(20,600,40):
        for x in range(20,600,40):
            pixel = pixels[y * 600 + x]
            if pixel not in [(105,204,212),(113,208,216)]:
                points.append([x//112,y//112,str(pixel)])
    return points
while True:
    test = getScreen()
    yes = pain.pain(test,5)
    paths = {}
    for dot in test:
        if dot[2] not in paths:
            paths[dot[2]] = [dot[:2]]
        else:
            paths[dot[2]].append(dot[:2])

    for e in yes:
        last = [paths[e][1][0] * 40 + 678 ,paths[e][1][1] * 40 + 233]
        mouse.move(paths[e][1][0] * 40 + 678 ,paths[e][1][1] * 40 + 233,absolute = True,duration=0.03)
        for cords in yes[e]:
            mouse.drag(last[0],last[1],cords[0] * 40 + 678,cords[1] * 40 + 233,absolute=True,duration=0.03)
            last = [cords[0] * 40 + 678,cords[1] * 40 + 233] 
        mouse.drag(last[0],last[1],paths[e][0][0] * 40 + 678 ,paths[e][0][1] * 40 + 233,absolute=True,duration=0.03)
    time.sleep(2)
        
        
