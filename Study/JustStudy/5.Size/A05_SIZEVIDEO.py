import cv2

cap = cv2.VideoCapture('../video.mp4')

while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break
    
    frame_resize = cv2.resize(frame, (100, 300)) # 영상 고정 크기 조절
    frame_resize2 = cv2.resize(frame, None, fx=0.5, fy=0.5) # 영상 비율로 크기 조절


    cv2.imshow('video', frame_resize2)

    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()