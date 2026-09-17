import cv2 as cv
import numpy as np

#Load face cascade and hair cascade from haarcascades folder
face_cascade = cv.CascadeClassifier("F:\quantanics\computer Vision\haarcascades face and eye detection\haarcascades\haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("F:\quantanics\computer Vision\haarcascades face and eye detection\haarcascades\haarcascade_eye.xml")

#Read image in img and convert it to grayscale and store in gray.
#Image is converted to grayscale, as face cascade doesn't require to operate on coloured images.
img = cv.imread(r"F:\quantanics\computer Vision\haarcascades face and eye detection\images\static_image3.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Detect all faces in image.
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#Draw a rectangle over the face, and detect eyes in faces
for (x,y,w,h) in faces:
    cv.putText(img, "Tamilnilavan.K", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    #ROI is region of interest with area having face inside it.
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    #Detect eyes in face
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex,ey,ew,eh) in eyes:
        #cv.putText(roi_color, "Tamilnilavan.K", (100, 300), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#cv.putText(img, "Tamilnilavan.K", (100, 300), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
cv.imshow('Image', img)
#cv.imwrite(r"F:\quantanics\computer Vision\haarcascades face and eye detection\output\output_image3.jpg", img)  # Save the output image
cv.waitKey(0)
cv.destroyAllWindows()
