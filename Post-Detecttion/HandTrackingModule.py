import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False,maxHands = 2, model_complex = 1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.model_complex = model_complex
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complex ,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHand(self, frame, draw = True):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                if draw == True:
                    self.mpDraw.draw_landmarks(frame, hand, self.mpHands.HAND_CONNECTIONS)
        return frame
    
    def findPosition(self, frame, handNo = 0):
        lmList = []
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if  results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[handNo]
            # for hand in results.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                h, w, c = frame.shape
                cx, cy = (lm.x * w), (lm.y * h)
                lmList.append({"id":id, "x":cx, "y":cy})
        return lmList


def main():
    try:

        cap = cv2.VideoCapture(0)
        hand = handDetector()
        while True:
            status, frame = cap.read()
            drawFrame = hand.findHand(frame)
            position = hand.findPosition(frame)
            if len(position) != 0:
                print(position[0])
            cv2.imshow('Hand', drawFrame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    except Exception as e:
        print(e)
        cv2.destroyAllWindows()

            
    


if __name__ == "__main__":
    main()