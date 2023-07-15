import cv2

img = cv2.imread("../img.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite('img_save.jpg', img) #내가 처리한 이미지를 저장하는 법