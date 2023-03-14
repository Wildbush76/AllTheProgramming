from PIL import ImageGrab
import mouse
import time
def findDa():
    screenshot = ImageGrab.grab(bbox = [682,376,1221,795])
    screenshot.save("yes.png")
    pixels = screenshot.getdata()
    board = []
    for y in range(15,419,30):
        coll = []
        for x in range(15,539,30):
            
            pixel = pixels[x + y*539]
            if pixel in [(185, 221, 119),(215, 184, 153),(168, 212, 80),(160, 206, 72),(229,194,159)]:
                coll.append(' ')
            elif pixel in [(162,209,73),(170,215,81)]:
                coll.append("?")
            elif pixel in [(25,118,210)]:
                coll.append('1')
            elif pixel in [(154, 171, 116),(60, 143, 62),(78,148,73),(80, 149, 74),(59, 143, 62),(70, 146, 68)]:
                coll.append('2')
            elif pixel in [(213, 65, 61),(211, 64, 60)]:
                coll.append('3')
            elif pixel in [(211, 178, 153)]:
                coll.append('4')
            elif pixel in [(254, 144, 4)]:
                coll.append('5')
            else:
                print(pixel)
                mouse.move(x + 682, y + 376)
                raise Exception ("your a idoit")
        board.append(coll)
    for hh in board:
        print(" ".join(hh))
    return board
def howManyIdiots(x,y,board):
    if len(board[0]) > x > 0 and len(board) > y > 0:
        if board[y][x] == "?":
            return 1
    return 0

def imBetterThanYou(flags):
    board = findDa()
    for y,row in enumerate(board):
        for x,val in enumerate(row):
            if val == " " or val == "?":
                continue
            neighbors = [0, 0]#flagged, total
            for yes in range(-1, 2):
                for no in range(-1, 2):
                    if (x + yes,y + no) in flags:
                        neighbors[0] += 1
                    else:
                        neighbors[1] += howManyIdiots(yes + x, no + y, board)
            if neighbors[1] == int(val):
                for xx in range(-1,2):
                    for yy in range(-1,2):
                        if howManyIdiots(x + xx,y + yy,board):
                            if (x + xx,y+yy) not in flags:
                                mouse.move((x + xx) * 30 + 697, (y + yy) * 30 + 391,True,0.25)
                                mouse.click("right")
                                flags.append((x + xx,y + yy))
                                return
            if neighbors[0] == int(val):
                mouse.move(x * 30 + 697, y * 30 + 391,True,0.25)
                mouse.click("middle")
                return
                
            
            
    
def main():
    mouse.move(682 + 255,376 + 199)
    mouse.click("left")
    time.sleep(0.5)
    flags = []
    while len(flags) != 40:
        imBetterThanYou(flags)
        print(flags)
        time.sleep(5)
    
main()
    
