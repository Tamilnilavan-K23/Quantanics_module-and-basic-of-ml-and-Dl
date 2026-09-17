import cv2 as cv

cap = cv.VideoCapture(r"C:\Users\Tamil\OneDrive\Pictures\Saved Pictures\videoplayback.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    #frameS = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  
    cv.imshow("Video", frame)
    #cv.imwrite("frame.jpg", frame)  
    if cv.waitKey(30) & 0xFF == 27:  
        break
   
cap.release()
cv.destroyAllWindows()

