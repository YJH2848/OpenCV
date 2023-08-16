import cv2

def empty(pos):
    print(pos)
    pass


img = cv2.imread('../books.jpg', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty) #bar의 이름과 창의 이름, 초기값, 최대값, 이벤트 처리 순서

while True:
    thresh = cv2.getTrackbarPos('threshold', name) #bar이름, 창이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    if not ret:
        break

    cv2.imshow(name, binary)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()