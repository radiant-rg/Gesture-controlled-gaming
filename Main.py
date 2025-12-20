
import cv2
import mediapipe
import traceback
import pyautogui


def show(landmark, frame, fw, fh):
    if landmark is not None:
        coor = mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(
            landmark.x, landmark.y, fw, fh
        )
        if coor is not None:
            frame = cv2.circle(frame, coor, 5, (0, 0, 255), -1)
    return frame



def count_fingers(hand_landmarks):
    tips = [
        mediapipe.solutions.hands.HandLandmark.THUMB_TIP,
        mediapipe.solutions.hands.HandLandmark.INDEX_FINGER_TIP,
        mediapipe.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP,
        mediapipe.solutions.hands.HandLandmark.RING_FINGER_TIP,
        mediapipe.solutions.hands.HandLandmark.PINKY_TIP
    ]

    pip = [
        mediapipe.solutions.hands.HandLandmark.THUMB_IP,
        mediapipe.solutions.hands.HandLandmark.INDEX_FINGER_PIP,
        mediapipe.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP,
        mediapipe.solutions.hands.HandLandmark.RING_FINGER_PIP,
        mediapipe.solutions.hands.HandLandmark.PINKY_PIP
    ]

    fingers = []


    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[pip[0]].x:
        fingers.append(1)
    else:
        fingers.append(0)


    for i in range(1, 5):
        if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[pip[i]].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)


def keybd(finger_count, frame):
    if finger_count == 1:
        pyautogui.keyUp("left")
        pyautogui.keyDown("right")
        cv2.putText(frame, "GAS", (40, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    elif finger_count == 0:
        pyautogui.keyUp("right")
        pyautogui.keyDown("left")
        cv2.putText(frame, "BRAKE", (40, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    else:
        pyautogui.keyUp("left")
        pyautogui.keyUp("right")
        cv2.putText(frame, "NEUTRAL", (40, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)


try:
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise Exception("Camera not found or can't be accessed.")

    fw = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    fh = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    with mediapipe.solutions.hands.Hands(
        static_image_mode=False,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_hands=1
    ) as hands:

        print("🚀 Hand gesture control started. Press ESC to exit.")
        print("One finger = GAS | Closed hand = BRAKE")

        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                continue

            frame = cv2.flip(frame, 1)
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]

                finger_count = count_fingers(hand_landmarks)
                keybd(finger_count, frame)


                mediapipe.solutions.drawing_utils.draw_landmarks(
                    frame, hand_landmarks, mediapipe.solutions.hands.HAND_CONNECTIONS
                )


                for lm in hand_landmarks.landmark:
                    frame = show(lm, frame, fw, fh)

                cv2.putText(frame, f"Fingers: {finger_count}", (20, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow("Hill Climb Controller", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    capture.release()
    cv2.destroyAllWindows()
    print("✅ Program exited cleanly.")

except Exception as e:
    traceback.print_exc()
    pyautogui.keyUp("left")
    pyautogui.keyUp("right")
    if 'capture' in locals():
        capture.release()
    cv2.destroyAllWindows()







