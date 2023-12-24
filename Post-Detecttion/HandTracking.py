import cv2
import mediapipe as mp
import time



try:
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    while True:
        initial_time = time.time()
        status, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        # print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                for id, lm in enumerate(hand.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id ,cx, cy)
                    if id in ([4, 8, 12, 16, 20]):
                        cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
        final_time = time.time()

        fps = 1 / (final_time - initial_time)

        cv2.putText(frame, str(f'FPS: {int(fps)}'), (10,40), cv2.FONT_HERSHEY_PLAIN,3,(255, 0, 0), 3)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) % 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break

except Exception as e:
    print(e)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
