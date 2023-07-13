import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)
RADIUS = 50 #반지름
THICKNESS = 10 #두께

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) #속이 빈 원

cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) #속이 꽉 찬 원


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()