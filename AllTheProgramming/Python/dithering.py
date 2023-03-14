from PIL import Image, ImageOps
image = ImageOps.grayscale(Image.open("test.jpg"))
width, height = image.size
pixels = list(image.getdata())
newpixels = []

for y in range(height):
    for x in range(width):
        oldPixel = pixels[x + y*width]
        newPixel = round(oldPixel/255)*255
        newpixels.append(newPixel)
        error = oldPixel - newPixel
        if x < width - 1:
            pixels[x + 1 + (y * width)] += error * (7/16)
            if y < height - 1:
                pixels[(x+1) + ((y+1)*width)] += error * (1/16)
        if y < height - 1:
            if x > 0:
                pixels[x - 1 + ((y+1)*width)] += error * (3/16)
            pixels[x + (y+1)*width] += error * (5/16)
newImage = Image.new(image.mode,image.size)
newImage.putdata(newpixels)
newImage.save("output.png")#and this is output

