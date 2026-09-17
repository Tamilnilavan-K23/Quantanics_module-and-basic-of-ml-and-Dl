import cv2 as cv

# Load Haar cascades
face_cascade = cv.CascadeClassifier(r"F:\quantanics\computer Vision\haarcascades face and eye detection\haarcascades\haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier(r"F:\quantanics\computer Vision\haarcascades face and eye detection\haarcascades\haarcascade_eye.xml")

# Start webcam
video_capture = cv.VideoCapture(0)
video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

# Reference face
reference_face = (221, 75, 340, 405)
recorded_name = "Tamilnilavan.K"

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    try:
        frame = cv.flip(frame, 1)
        frame = cv.resize(frame, (1280, 720))
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            try:
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            except Exception as eye_error:
                print("Eye detection error:", eye_error)

            rx, ry, rw, rh = reference_face
            if abs(x - rx) < 40 and abs(y - ry) < 40 and abs(w - rw) < 40 and abs(h - rh) < 40:
                cv.putText(frame, recorded_name, (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            else:
                cv.putText(frame, "Another person", (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    except Exception as main_error:
        print("Main processing error:", main_error)

    cv.imshow('Live Recognition', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
