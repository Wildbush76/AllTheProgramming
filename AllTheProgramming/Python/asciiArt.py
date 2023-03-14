from PIL import Image, ImageOps

image = ImageOps.grayscale(Image.open("cat.JPG"))
width, height = image.size

maxHeight = 600
maxWidth = 600
if height > maxHeight or width > maxWidth:
    if height > width:
        ratio = maxHeight/height
    else:
        ratio = maxWidth/width
    image = image.resize((int(width * ratio),int(height * ratio)))
    width, height = image.size

pixels = list(image.getdata())
newpixels = []

characterSet = "C "

num = len(characterSet)-1
for y in range(height):
    for x in range(width):
        oldPixel = pixels[x + y*width]
        newPixel = round((oldPixel / 255) * num) * (255 / num)
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
    
with open("output.txt","w") as file:
    output = ""
    for index, pixel in enumerate(newpixels):
        if index % width == 0:
            output += "\n"
        output += characterSet[int(pixel / 255*num)]
    file.write(output)

print("we done here boys")
