import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)
THICKNESS = 10 #두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
cv2.fillPoly(img, [pts1],  COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()