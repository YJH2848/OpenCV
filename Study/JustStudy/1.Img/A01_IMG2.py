import cv2

img_color = cv2.imread('../img.jpg', cv2.IMREAD_COLOR) #컬러 이미지 가져옴 (기본값)
img_gray = cv2.imread('../img.jpg', cv2.IMREAD_GRAYSCALE) #흑백 이미지 가져옴
img_unchanged = cv2.imread('../img.jpg', cv2.IMREAD_UNCHANGED) #투명 이미지 가져옴

img = cv2.imread('../img.jpg')

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)

print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()