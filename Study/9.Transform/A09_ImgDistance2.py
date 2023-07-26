import cv2
import numpy as np
img = cv2.imread('../pokerCard.jpg')

width, height = 530, 710

src = np.array([[706, 148],[1138, 421],[718, 1017],[280, 697]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32) # output 4개 지정

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height)) #matrix대로 변환를 함

cv2.imshow('img', result)

cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()