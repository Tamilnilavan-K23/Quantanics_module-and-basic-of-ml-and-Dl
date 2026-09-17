import cv2
import mediapipe as mp
import pyautogui
import time
import os

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
   # frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        # Index finger tip (landmark 8)
        index_finger_tip = hand_landmarks.landmark[8]
        x = int(index_finger_tip.x * w)
        y = int(index_finger_tip.y * h)

        # Draw circle at index fingertip
        cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

        # Map webcam coordinates to screen coordinates
        screen_x = int(index_finger_tip.x * screen_width)
        screen_y = int(index_finger_tip.y * screen_height)

        # Draw hand landmarks
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Count fingers (just index and middle for demo)
        if lm[8].y < lm[6].y:  # Index finger
            finger_count += 1
        if lm[12].y < lm[10].y:  # Middle finger
            finger_count += 1

        # Action based on fingers
        if finger_count == 1:
            pyautogui.moveTo(screen_x, screen_y)
            cv2.putText(frame, "Move Mouse", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        elif finger_count == 2:
            pyautogui.click()
            cv2.putText(frame, "Click", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
       
        else:
            cv2.putText(frame, "Show your hand...", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    frame=cv2.resize(frame, (1920, 1080))
    cv2.imshow("PyAutoGUI Demo", frame)

    if cv2.waitKey(1) ==27:
        break

cap.release()
cv2.destroyAllWindows()


""""
        elif finger_count == 5:
            os.open("notepad.exe")
            cv2.putText(frame, "Open Notepad", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            time.sleep(2)
            pyautogui.write("Hello from PyAutoGUI!", interval=0.1)
"""""