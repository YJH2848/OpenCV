import cv2

img = cv2.imread('../img.jpg')

flip_horizontal = cv2.flip(img, 1) #1은 좌우대칭 filpcode가 0보다 크면 무조건 좌우대칭(수평) 0은 상하대칭
flip_vertical = cv2.flip(img, 0) #0은 상하대칭
flip2 = cv2.flip(img, -1)  #filp이 0보다 작으면 상하좌우 대칭

cv2.imshow('filp_horizontal', flip_horizontal)
cv2.imshow('flip_vertical', flip_vertical)
cv2.imshow('flip2', flip2)

cv2.waitKey(0)
cv2.destroyAllWindows()