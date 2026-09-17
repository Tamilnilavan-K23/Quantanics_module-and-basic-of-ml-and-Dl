import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

prev_gesture = None
gesture_cooldown = 1  # seconds
last_time = time.time()

def count_fingers(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    # Thumb (based on x)
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (based on y)
    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(hand_landmarks)

            # Cooldown check
            if time.time() - last_time > gesture_cooldown:
                if finger_count == 2 and prev_gesture != "switch":
                    pyautogui.hotkey('alt', 'tab')
                    prev_gesture = "switch"
                    last_time = time.time()
                elif finger_count == 0 and prev_gesture != "minimize":
                    pyautogui.hotkey('win', 'down')
                    prev_gesture = "minimize"
                    last_time = time.time()
                elif finger_count == 5 and prev_gesture != "maximize":
                    pyautogui.hotkey('win', 'up')
                    prev_gesture = "maximize"
                    last_time = time.time()

    else:
        prev_gesture = None

    cv2.imshow("Window Control with Hand Gestures", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
