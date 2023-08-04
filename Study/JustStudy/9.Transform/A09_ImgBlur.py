#커널 사이즈에 변화에 따른 흐림
import cv2
img = cv2.imread('../img.jpg')

# (3, 3) (5, 5) (7, 7)에 대한 커널사이즈가 우수한 성능을 보여주기 떄문에 쓴다.
kernel_3 = cv2.GaussianBlur(img, (3, 3), 0)
kernel_5 = cv2.GaussianBlur(img, (5, 5), 0)
kernel_7 = cv2.GaussianBlur(img, (7, 7), 0)

# 표준 편차에 따른 흐림 처리 (시그마x - 가우시안 커널의 x 방향의 표준편차)
sigma_1 = cv2.GaussianBlur(img, (0, 0), 1)
sigma_2 = cv2.GaussianBlur(img, (0, 0), 2)
sigma_3 = cv2.GaussianBlur(img, (0, 0), 3)

cv2.imshow('img1', sigma_1)
cv2.imshow('img2', sigma_2)
cv2.imshow('img3', sigma_3)
cv2.waitKey(0)
cv2.destroyAllWindows()