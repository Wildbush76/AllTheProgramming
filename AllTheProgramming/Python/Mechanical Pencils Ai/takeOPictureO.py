import cv2
import time

cap = cv2.VideoCapture(0)

yes = 0


while True:
    print("frame")
    ret, frame = cap.read()
    cv2.imwrite(f"imageTHing/lolz{yes}.png",frame)
    yes += 1
    
