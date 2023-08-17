import cv2
import numpy as np

point_list = []
width, height = 530, 710
Color = (255, 0, 255)
THICKNESS = 3
drawing = False #선 그릴지 여부

src_img = cv2.imread('pokerCard.jpg')

def mouse_handler(event, x, y, flags, param):
    global drawing

    dst_img = src_img.copy() #사진 사본 복사

    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append((x, y))
        drawing = True #선을 그리기 시작
        
    if drawing:
        prev_point = None #직선의 시작 점
        for point in point_list:
            cv2.circle(dst_img, point, 10, Color, cv2. FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, Color, THICKNESS, cv2.LINE_AA)
            prev_point = point

        next_point = (x, y)
        if len(point_list) == 4:
            show_result()
            next_point = point_list[0] #첫번쨰 클릭한 점 
        cv2.line(dst_img, prev_point, next_point, Color, THICKNESS, cv2.LINE_AA)
        

    cv2.imshow('img', dst_img)


def show_result():
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(src_img, matrix, (width, height))


    cv2.imshow('result', result)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()