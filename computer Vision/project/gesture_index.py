import cv2
import mediapipe as mp
import pyautogui
import pyttsx3
import time

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# Initialize pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Open webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

last_action_time = 0
action_delay =  0.5 # seconds
last_action = ""

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
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            if lm_list:
                ix, iy = lm_list[8]  # Index finger tip
                cv2.circle(frame, (ix, iy), 10, (255, 0, 255), cv2.FILLED)

                current_time = time.time()

                if current_time - last_action_time > action_delay:
                    if iy < h // 3 and last_action != "up":
                        pyautogui.hotkey('win', 'up')
                        speak("Window moved up")
                        last_action = "up"
                        last_action_time = current_time
                    elif iy > 2 * h // 3 and last_action != "down":
                        pyautogui.hotkey('win', 'd')
                        speak("Window moved down")
                        last_action = "down"
                        last_action_time = current_time
                    elif ix < w // 3 and last_action != "left":
                        pyautogui.hotkey('win', 'left')
                        speak("Window moved left")
                        last_action = "left"
                        last_action_time = current_time
                    elif ix > 2 * w // 3 and last_action != "right":
                        pyautogui.hotkey('win', 'right')
                        speak("Window moved right")
                        last_action = "right"
                        last_action_time = current_time

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Kural - Window Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
