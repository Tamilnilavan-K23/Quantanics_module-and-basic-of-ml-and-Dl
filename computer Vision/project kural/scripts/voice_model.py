import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import pyttsx3


model = tf.keras.models.load_model(r"F:\quantanics\computer Vision\project kural\model\face_recognition_model.h5")
CLASS_NAMES = ['tamilnilavan']  


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)  
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tamil')  


assistant_name = "Kural"

def speak(text):
    engine.say(text)
    engine.runAndWait()


cap = cv2.VideoCapture(0)
already_greeted = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    face = cv2.resize(frame, (224, 224))
    face = img_to_array(face) / 255.0
    face = np.expand_dims(face, axis=0)

    preds = model.predict(face)[0]
    confidence = np.max(preds)
    name = CLASS_NAMES[np.argmax(preds)]

    if confidence > 0.90:
        cv2.putText(frame, f"Hello, {name}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if not already_greeted:
            speak(f"Vanakkam {name}. I am {assistant_name}, your personal voice assistant.")
            already_greeted = True
    else:
        cv2.putText(frame, "Unknown", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        already_greeted = False

    cv2.imshow("Kural - Face Assistant", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
