import cv2

# Load the full body and upper body cascade classifiers
full_body_cascade = cv2.CascadeClassifier('F:\quantanics\Computer_Vision_git\Opencv\Full and Partial Body Detection\haarcascades_fullbody.xml')
upper_body_cascade = cv2.CascadeClassifier('F:\quantanics\Computer_Vision_git\Opencv\Full and Partial Body Detection\haarcascade_upperbody.xml')
lower_body_cascade = cv2.CascadeClassifier('F:\quantanics\Computer_Vision_git\Opencv\Full and Partial Body Detection\haarcascade_lowerbody.xml')

# Function to detect and draw bodies
def detect_and_draw_bodies(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    full_bodies = full_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    upper_bodies = upper_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    lower_bodies = lower_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in full_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in upper_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in lower_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    return img

# Detect bodies in an image
image = cv2.imread('F:\quantanics\Computer_Vision_git\Opencv\Full and Partial Body Detection\image1.jpg')
result_image = detect_and_draw_bodies(image)
cv2.imshow('Full and Lower Body Detection in Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detect bodies through camera feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    
    result_frame = detect_and_draw_bodies(frame)
    result_frame = cv2.resize(result_frame, (333, 500))  # Resize for better visibility
    cv2.imshow('Full and Lower Body Detection in Camera', result_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
