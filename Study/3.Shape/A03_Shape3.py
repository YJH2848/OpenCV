import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 255)
THICKNESS = 20 #두께
 
cv2.line(img, (50, 50), (400, 50), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 100), (400, 100), COLOR, THICKNESS, cv2.LINE_8)  
cv2.line(img, (50, 150), (400, 150), COLOR, THICKNESS, cv2.LINE_AA)
#그릴 위치 :img, 50,100을 시작지점으로 400, 50까지 끄어버린다, 색은 노랑, 선 두께는 3, 선 종류는 기본값

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()