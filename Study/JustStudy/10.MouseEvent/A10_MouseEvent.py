import cv2

def mouse_handler(event, x, y, flags, param): #마우스 이벤트 처리하는 곳
    if event == cv2.EVENT_LBUTTONDOWN:#마우스 왼쪽 버튼
        print('왼쪽 버튼 클릭!')
        print('x좌표는 =', x, '이고 y좌표는 = ', y)
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼 클릭!')
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('왼쪽 버튼 두번 클릭!')
    elif event == cv2.EVENT_MOUSEMOVE:
        print("마우스 움직임!")
           
img = cv2.imread('ACard.png')

cv2.namedWindow('img') #img라는 이름의 윈도우를 만들어 둠 여기에 마우스 이벤트 처리하기 위한 헨들러 적용
cv2.setMouseCallback('img', mouse_handler)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()