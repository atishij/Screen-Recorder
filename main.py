from PIL import ImageGrab
import numpy as np
import cv2

while True:
    #width of the box and origin coordinates(0,0)
    img = ImageGrab.grab(bbox=(0, 0, 1000, 520))
    img_np = np.array(img)
    # For exact colors
    img_final = cv2.cvtColor(img_np , cv2.COLOR_BGR2RGB)
    # Title of the box and printing the box
    cv2.imshow('Secret Capture' , img_final)
