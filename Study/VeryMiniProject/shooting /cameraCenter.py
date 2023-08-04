import cv2

def draw_center_point(frame):
    height, width, _ = frame.shape
    center_x = width // 2
    center_y = height // 2
    cv2.circle(frame, (center_x, center_y), 4, (0, 255, 0), -1)

def main():
    cap = cv2.VideoCapture(0) 
    
    if not cap.isOpened():
        return
    
    while True:
        ret, frame = cap.read() 
        
        if not ret:
            break
        draw_center_point(frame)
        cv2.imshow('Camera', frame) 
        if cv2.waitKey(1) == ord('q'): 
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
