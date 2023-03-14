from PIL import ImageGrab, ImageOps
bbox = [612,330,1286,854]
def find():
    screenshot = ImageGrab.grab(bbox = bbox)
    file = open("image.png","w")
    file.write(screenshot)
    file.close()
