import cv2
import numpy as np

point_list = []
width, height = 530, 710
Color = (255, 0, 255)
src_img = cv2.imread('pokerCard.jpg')

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append((x, y))
        
    for point in point_list:
        cv2.circle(src_img, point, 10, Color, cv2. FILLED)

    if len(point_list) == 4:
        show_result()

    cv2.imshow('img', src_img)


def show_result():
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(src_img, matrix, (width, height)) #matrix대로 변환를 함


    cv2.imshow('result', result)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()