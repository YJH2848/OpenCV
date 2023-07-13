import cv2
import numpy as np

#세로 480, 가로 640, 채널은 3(rgb)에 해당하는 스케치
img = np.zeros((480, 640, 3), dtype=np.uint8)
img[:] = (255,255,255) #전체 공간을 흰색으로 채우기 (BGR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)