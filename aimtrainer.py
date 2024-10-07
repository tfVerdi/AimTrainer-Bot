import cv2
import numpy as np
from PIL import ImageGrab
import mouse
import keyboard
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(2)
diana = cv2.imread("assets//diana.jpg")
for i in diana:
    for n in i:
        n[2], n[1], n[0] = n
cv2.imshow("Diana", diana)
cv2.waitKey()
cv2.destroyAllWindows()
canvas = cv2.imread("assets//canvas.jpg")
print(diana.shape)
h, w, _ = diana.shape

while True:
    print("working")
    canvas = np.array(ImageGrab.grab(bbox=(0, 190, 1920, 1000)))
    matches = cv2.matchTemplate(canvas, diana, cv2.TM_CCOEFF_NORMED)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matches)
    if maxVal>=0.70:
        # cv2.rectangle(canvas, maxLoc, (maxLoc[0]+w,maxLoc[1]+h),(255,255,255),2)
        # cv2.imshow("Canvas", canvas)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        mouse.move(maxLoc[0] + (w/2), maxLoc[1] + 270, absolute=True)
        mouse.click()
    if keyboard.is_pressed("esc"):
        break