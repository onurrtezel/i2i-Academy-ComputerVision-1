import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Finger tip and joint landmark indices
TIPS = [4, 8, 12, 16, 20]
JOINTS = [3, 6, 10, 14, 18]

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    total = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, lm in enumerate(results.multi_hand_landmarks):
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)
            label = results.multi_handedness[i].classification[0].label

            # Thumb: compare x-axis based on hand label
            if (label == "Right" and lm.landmark[4].x < lm.landmark[3].x) or \
               (label == "Left" and lm.landmark[4].x > lm.landmark[3].x):
                total += 1

            # Other 4 fingers: tip above joint means open
            total += sum(1 for t, j in zip(TIPS[1:], JOINTS[1:]) if lm.landmark[t].y < lm.landmark[j].y)

    cv2.putText(frame, f"Fingers: {total}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("i2i Academy - Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
