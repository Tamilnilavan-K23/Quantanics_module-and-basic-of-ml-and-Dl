import cv2 as cv

cap= cv.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    cv.imshow("Video", frame)
    if cv.waitKey(30) & 0xff ==27:
        break

cap.release()
cv.destroyAllWindows()