import cv2

# Load the mouth cascade classifier
mouth_cascade = cv2.CascadeClassifier('mouth.xml')

# Function to detect and draw mouths
def detect_and_draw_mouths(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mouths = mouth_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in mouths:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return img

# Detect mouths in an image
image = cv2.imread('test.jpeg')
result_image = detect_and_draw_mouths(image)
cv2.imshow('Mouth Detection in Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detect mouths through camera feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    result_frame = detect_and_draw_mouths(frame)
    cv2.imshow('Mouth Detection in Camera', result_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
