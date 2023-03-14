from PIL import Image
import os
try:
    os.remove("thing.gcode")
except:
    print("remove failed")
theThing = Image.open("someone.png")
width, height = theThing.size

start = (20,70)
pixels = theThing.getdata()
with open("thing.gcode","a") as file:
    file.write("G28\n G1 Z10")
    for y in range(height):
        for x in range(width):
            if pixels[y * width + x] == 255:
                continue
            file.write(f"G0 F4000 X{x + start[0]} Y{y + start[1]}\n")
            file.write(f"G1 Z0\n")
            file.write(f"G1 Z4\n")
print("done path made")
