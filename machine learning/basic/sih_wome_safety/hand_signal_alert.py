import cv2
import mediapipe as mp
from twilio.rest import Client
import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

account_sid = 'ACb1c091435494334bb9e629e941a0cc77'
auth_token = '2d0ca7a8647da12c82013d9b70becf6d'
twilio_from_number = '+12202411149'
to_number = '+918925775915'

def detect_gesture(hand_dict):
    tips = [8, 12, 16, 20]
    fingers_open = 0
    for tip in tips:
        if hand_dict[tip][2] < hand_dict[tip - 2][2]:
            fingers_open += 1
    return "Open" if fingers_open >= 4 else "Close"

gesture_sequence = []
danger_detected = False

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            hand_dict = {}
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_dict[id] = (id, cx, cy)

            if hand_dict:
                gesture = detect_gesture(hand_dict)

                if len(gesture_sequence) == 0 or gesture_sequence[-1] != gesture:
                    gesture_sequence.append(gesture)
                    print(f"Gesture detected: {gesture}")

                if len(gesture_sequence) >= 4 and gesture_sequence[-4:] == ['Open', 'Close', 'Open', 'Close']:
                    danger_detected = True
                    print("DANGER DETECTED")
                    
                    speak('Danger detected for Dharani.')

                    client = Client(account_sid, auth_token)
                    twiml_message = """<Response>
    <Say voice="alice"><![CDATA[ Danger detected for Dharani ]]></Say>
</Response>"""

                    call = client.calls.create(
                        twiml=twiml_message,
                        to=to_number,
                        from_=twilio_from_number
                    )
                    print(f"Call SID: {call.sid}")

                    time.sleep(5)
                    break

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if danger_detected:
        break

cap.release()
cv2.destroyAllWindows()