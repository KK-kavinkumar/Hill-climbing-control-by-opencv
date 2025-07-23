import cv2
import mediapipe as mp
import pyautogui
import time

# Init webcam and MediaPipe
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.7)
tip_ids = [4, 8, 12, 16, 20]

# Track press state
accelerating = False
braking = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(rgb)

    gesture = "none"

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            # Get landmarks
            lm = hand.landmark
            fingers = []

            # Thumb
            if lm[tip_ids[0]].x < lm[tip_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for id in range(1, 5):
                if lm[tip_ids[id]].y < lm[tip_ids[id] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = sum(fingers)

            # Detect gestures
            if total == 1 and fingers[1] == 1:
                gesture = "brake"
                if not braking:
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('right')
                    braking = True
                    accelerating = False
            elif total == 5:
                gesture = "accelerate"
                if not accelerating:
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('left')
                    accelerating = True
                    braking = False
            elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
                gesture = "cursor_move"
                index_finger = lm[8]
                screen_x = int(index_finger.x * pyautogui.size().width)
                screen_y = int(index_finger.y * pyautogui.size().height)
                pyautogui.moveTo(screen_x, screen_y)
                # Release keys when cursor control
                pyautogui.keyUp('left')
                pyautogui.keyUp('right')
                accelerating = braking = False
            elif total <= 1:
                gesture = "enter"
                pyautogui.press('enter')
                # Reset
                pyautogui.keyUp('left')
                pyautogui.keyUp('right')
                accelerating = braking = False
                time.sleep(0.5)  # Delay to avoid multiple presses

    else:
        # No hand = release everything
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
        accelerating = braking = False

    # Display
    cv2.putText(frame, f"Gesture: {gesture}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Hill Climb - Full Hand Gesture Control", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
pyautogui.keyUp('left')
pyautogui.keyUp('right')
