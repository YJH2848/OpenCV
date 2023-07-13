import cv2

cap = cv2.VideoCapture(0) #0번째 카메라 아이디이다.

if not cap.isOpened(): #카메라 열기 실패했을 경우
    print("프로그램을 종료하겠습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()