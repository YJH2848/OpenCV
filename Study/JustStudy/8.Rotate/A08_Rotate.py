import cv2

img = cv2.imread('../img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #시계방향으로 90도회전
rotate_180 = cv2.rotate(img, cv2.ROTATE_180) #시계방향으로 180도회전


cv2.imshow('img',rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows()