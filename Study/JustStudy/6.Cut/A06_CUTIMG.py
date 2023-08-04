import cv2

#이거는 새로운 윈도우 창에 띄운 방법
img = cv2.imread('../img.jpg')

crop = img[100:200, 200:400] #세로범위, 가로범위

cv2.imshow('cut', img)
cv2.imshow('cut2', crop)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 기존의 창에 추가적으로 뛰우는 방법
img = cv2.imread('../img.jpg')

crop = img[100:200, 200:400] #세로범위, 가로범위
img[100:200, 400:600] = crop

cv2.imshow('cut', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

