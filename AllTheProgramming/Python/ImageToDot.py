from PIL import Image, ImageOps
import copy
file = open("output.txt","w")
wanted = 100
image = ImageOps.grayscale(Image.open("test.png"))
width, height = image.size
resize = wanted / max(width,height)
image = image.resize((round(width*resize),round(height*resize)))
width, height = image.size
pixels = list(image.getdata())
output = ""
for y in range(height-1):
    row = ""
    for x in range(width-1):
        oldPixel = pixels[x + y*width]
        newPixel = round(oldPixel/255)*255
        if newPixel <= 0:
            row += "o"
        else:
            row += " "
        error = oldPixel - newPixel
        if x < width - 1:
            pixels[x + 1 + (y * width)] += error * (7/16)
            if y < height - 1:
                pixels[(x+1) + ((y+1)*width)] += error * (1/16)
        if y < height - 1:
            if x > 0:
                pixels[x - 1 + ((y+1)*width)] += error * (3/16)
            pixels[x + (y+1)*width] += error * (5/16)
    print(row)
    output += row + "\n"
file.write(output)
file.close()

