import cv2
import requests
import numpy as np
import imutils
from tensorflow.keras.models import load_model

# Load models
age_model = load_model(r'F:\quantanics\computer Vision\haascascade\model\age_model.h5')
gender_model = load_model(r'F:\quantanics\computer Vision\haascascade\model\gender_model.h5')

# Gender list for indexing
gender_list = ["Male", "Female"]

# Haar cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\Dhaarani S\Downloads\haarcascade_frontalface_default.xml")

# IP webcam URL
url = "http://192.168.1.22:8080/shot.jpg"

# Counters
total_faces = set()
male_count = 0
female_count = 0
frame_count = 0
person_id = 0

while True:
    # Get the frame from IP webcam
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    frame_count += 1
    if frame_count % 2 != 0:
        continue

    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        face_input = cv2.resize(face_img, (64, 64))
        face_input = face_input.astype('float32') / 255.0
        face_input = np.expand_dims(face_input, axis=0)

        # Predict gender
        gender_pred = gender_model.predict(face_input)
        gender = gender_list[np.argmax(gender_pred)]

        # Predict age
        age_pred = age_model.predict(face_input)
        age = int(age_pred[0][0])  # assuming single neuron output (regression)

        # Track faces using unique bounding box location
        face_id = (x // 10, y // 10)  # Simple way to reduce duplicate counting
        if face_id not in total_faces:
            total_faces.add(face_id)
            if gender == "Male":
                male_count += 1
            else:
                female_count += 1

        label = f"{gender}, Age: {age}"
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Final report
print("=== Final Person Statistics ===")
print(f"Total Persons Detected: {len(total_faces)}")
print(f"Male Count: {male_count}")
print(f"Female Count: {female_count}")
