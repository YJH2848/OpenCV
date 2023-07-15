import cv2

cap = cv2.VideoCapture('../video.mp4')

#코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #영상의 WIDTH값을 가져옴
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #영상의 HEIGHT값을 가져옴
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret :
        break

    out.write(frame) #영상데이터만 저장 (소리x)

    cv2.imshow('video', frame)

    if cv2.waitKey(0) == ord('q'):
        break

out.release() #자원해제
cap.release()
cv2.destroyAllWindows()