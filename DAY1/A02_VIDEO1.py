import cv2
cap = cv2.VideoCapture('video.mp4') #video.mp4가져와서 cap에 넣어줌

while cap.isOpened(): #동영상이 열렸는지 확인
    ret, frame = cap.read() #ret는 성공여부, 성공하면 frame값이 저장됨
    if not ret:
        print('더 이상 가져올 프레임이 없어요')
        break

    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == ord('q'): #키 값 비교할때 ord
        print('사용자 입력에 의해 종료합니다.')
        break

cap.release() #자원 해제
cv2.destroyAllWindows()