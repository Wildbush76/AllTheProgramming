from PIL import ImageOps, Image
import numpy as np


# start doing it
print("starting")
theImage = ImageOps.grayscale(Image.open("cat.png"))

# convert to only black and white
pixels = np.array(theImage.getdata(), dtype=np.uint8)
newP = []
size = theImage.size
for y in range(size[1]):
    for x in range(size[0]):
        location = y * size[0] + x
        oldPixel = pixels[location]
        newP.append(round(pixels[location]/255)*255)
        pixels[location] = round(pixels[location]/255)*255
        error = oldPixel - int(pixels[location])

        if x < size[0] - 1:
            pixels[location + 1] += error * (7/16)
        elif x > 0:
            pixels[location - 1] += error * (3/16)
        if y < size[1]-1:
            pixels[location + size[0]] += error * (5/16)
        elif y > 0:
            pixels[location - size[0]] += error * (1/6)

newI = Image.new(theImage.mode, size)
newI.putdata(newP)

newI.save("new.png")
print("ive done it")
