from PIL import Image,ImageOps
photo = ImageOps.grayscale(Image.open("asdf.jfif"))
pixels = photo.load()
width,height = photo.size
for y in range(height):
    for x in range(width):
        oldPixel = pixels[x,y]
        pixels[x,y] = round(oldPixel/255)*255
        error = int(oldPixel - pixels[x,y])
        if x < width - 1:
            pixels[x + 1,y] += int(error * (7/16))
            if y < height - 1:
                pixels[x + 1,y] += int(error * (1/16))
        if y < height - 1:
            if x > 0:
                pixels[x - 1,y + 1] += int(error * (3/16))
            pixels[x,y + 1] += int(error * (5/16))
photo.show()
