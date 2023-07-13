# Opencv는 Computer Vision의 줄임말
# 다양한 영상 (이미지) / 동영상 처리에 사용되는 오픈소스 라이브러리이다.
#_________________________________________________________

import cv2
img = cv2.imread('img.jpg') #img.jpg를 읽어온다.
cv2.imshow('img', img) #img라는 화면에 띄운다
key = cv2.waitKey(0) #지정된 시간동안 키 입력대기 (0)은 무한 대기
print(key) #이렇게 변수에 waitKey를 넣으면 내가 무슨 키를 눌렀는지 아스키 코드로 나오게 된다.
cv2.destroyAllWindows() #모든 창을 끈다
