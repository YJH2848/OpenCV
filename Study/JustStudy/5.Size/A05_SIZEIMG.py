import cv2

img = cv2.imread('../img.jpg')
dst = cv2.resize(img, (400, 500)) #width, height 고정 크기 조절
dst2 = cv2.resize(img, None, fx=1.5, fy=1.5) #width, height 비율을 0.5배로 축소

cv2.imshow('resize', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()