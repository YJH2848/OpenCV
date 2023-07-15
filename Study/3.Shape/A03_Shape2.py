#일부 영역만 채우기import cv2
import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
img[:] = (255,255,255) 

img[100:300, 100:300] = (255, 0, 0) #좌측 끝을 기준으로 세로를 100에서 300사이, 가로를 100에서 300사이를 색을 파랑으로 칠한다.

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)