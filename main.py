import cv2
import mediapipe as mp

# setup mediapipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = 0

    if result.multi_hand_landmarks:
        for i in range(len(result.multi_hand_landmarks)):
            hand = result.multi_hand_landmarks[i]
            label = result.multi_handedness[i].classification[0].label
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            # check thumb
            if label == "Right":
                if hand.landmark[4].x < hand.landmark[3].x:
                    finger_count += 1
            else:
                if hand.landmark[4].x > hand.landmark[3].x:
                    finger_count += 1

            # check other fingers
            tips = [8, 12, 16, 20]
            joints = [6, 10, 14, 18]
            for t, j in zip(tips, joints):
                if hand.landmark[t].y < hand.landmark[j].y:
                    finger_count += 1

    cv2.putText(frame, "Fingers: " + str(finger_count), (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
