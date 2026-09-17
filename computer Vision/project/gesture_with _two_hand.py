import cv2
import mediapipe as mp
import pyautogui
import time
import pyttsx3
import os

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()
gesture_cooldown = time.time()
last_action = ""

cap = cv2.VideoCapture(0)
#cap=cv2.set(cv2.CAP_PROP_FPS,60)

def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []
    for tip in tips:
        if tip == 4:
            fingers.append(1 if hand_landmarks.landmark[tip].x < hand_landmarks.landmark[tip - 1].x else 0)
        else:
            fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)
    return fingers

def is_swipe(start, end, axis='x'):
    if axis == 'x':
        return abs(start[0] - end[0]) > 0.3 and abs(start[1] - end[1]) < 0.2
    else:
        return abs(start[1] - end[1]) > 0.3 and abs(start[0] - end[0]) < 0.2

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

screen_w, screen_h = pyautogui.size()
last_action = None

def perform_action(right_fingers, left_fingers, right_hand, left_hand):
    global last_action

    # Right hand all fingers down → Close current window
    if right_fingers == [0, 0, 0, 0, 0] and last_action != "Close Window":
        pyautogui.hotkey('win', 'd')
        speak("Window closed")
        time.sleep(1)
        last_action = "Close Window"

    # Right hand all fingers up → Open new window (Run Dialog)
    elif right_fingers == [1, 1, 1, 1, 1] and last_action != "Open Window":
        pyautogui.hotkey('alt', 'tab')
        speak("Opening run window")
        time.sleep(1)
        last_action = "Open Window"

    # Right hand swipe right to left → Move window to left
    elif right_fingers == [1, 1, 1, 1, 1] and last_action != "Snap Left":
        pyautogui.hotkey('win', 'left')
        speak("Window moved to left")
        time.sleep(1)
        last_action = "Snap Left"

    # Left hand swipe left to right → Move window to right
    elif left_fingers == [1, 1, 1, 1, 1] and last_action != "Snap Right":
        pyautogui.hotkey('win', 'right')
        speak("Window moved to right")
        time.sleep(1)
        last_action = "Snap Right"

    # Right hand only index finger up → Move mouse
    elif len(right_fingers) >= 3 and right_fingers[1] == 1 and all(f == 0 for i, f in enumerate(right_fingers) if i != 1):
        if right_hand and len(right_hand) > 8:
            cx = int(right_hand[8][0] * screen_w)
            cy = int(right_hand[8][1] * screen_h)
            pyautogui.moveTo(cx, cy)
            if last_action != "Mouse Move":
                speak("Moving mouse")
                time.sleep(1)
                last_action = "Mouse Move"

    # Right hand only middle finger up → Mouse click
    elif len(right_fingers) >= 3 and right_fingers[2] == 1 and all(f == 0 for i, f in enumerate(right_fingers) if i != 2):
        pyautogui.click()
        if last_action != "Mouse Click":
            speak("Mouse clicked")
            time.sleep(1)
            last_action = "Mouse Click"

    # Left hand index and pinky up → Open Edge browser
    elif len(left_fingers) >= 5 and left_fingers[1] == 1 and left_fingers[4] == 1 and all(left_fingers[i] == 0 for i in [0, 2, 3]) and last_action != "Open Edge":
        os.system("start msedge")
        speak("Opening Microsoft Edge")
        time.sleep(1)
        last_action = "Open Edge"

    gesture_cooldown = time.time()

while True:
    success, frame = cap.read()
    if not success:
        break
    #frame = cv2.flip(frame, 1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    right_hand, left_hand = None, None
    right_fingers, left_fingers = [], []

    if results.multi_hand_landmarks:
        for i, hand_landmark in enumerate(results.multi_hand_landmarks):
            lm = hand_landmark.landmark
            hand_type = results.multi_handedness[i].classification[0].label
            finger_state = count_fingers(hand_landmark)
            wrist = (lm[0].x, lm[0].y)
            index_tip = (lm[8].x, lm[8].y)

            if hand_type == 'Right':
                right_hand = (wrist, index_tip)
                right_fingers = finger_state
            else:
                left_hand = (wrist, index_tip)
                left_fingers = finger_state

            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

    perform_action(right_fingers, left_fingers, right_hand, left_hand)

    cv2.putText(frame, f"Action: {last_action}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 2)
    cv2.imshow("Two-Hand Gesture Control", frame)

    if cv2.waitKey(1) ==27:
        break

cap.release()
cv2.destroyAllWindows()


