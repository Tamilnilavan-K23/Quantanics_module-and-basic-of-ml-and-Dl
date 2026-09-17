import cv2
import numpy as np
from tensorflow.keras.models import load_model

def prediction(image, model):
    img = cv2.resize(image, (28, 28))
    img = img / 255
    img = img.reshape(1, 28, 28, 1)
    predict = model.predict(img)
    prob = np.amax(predict)
    class_index = np.argmax(predict, axis=1)[0]
    result = class_index
    if prob < 0.75:
        result = 0
        prob = 0
    return result, prob

model = load_model('digits.h5')

# Load the image
image_path = 'F:/Python/Open cv/7.jpg'
frame = cv2.imread(image_path)
frame_copy = frame.copy()

# Preprocess the image for digit recognition
img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (28, 28))
cv2.imshow("cropped", img_gray)

digit, probability = prediction(img_gray, model)
print(f"Recognized digit: {digit} with probability: {probability:.2f}")

cv2.imshow("input", frame_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
