import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from button import Button
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", " "],["Enter"]]
text = ''

buttonList = []
for bar in range(len(keys)):
    for eachkey in range(len(keys[bar])):
        if bar == 3 and eachkey == 0:
            buttonList.append(Button([100 * eachkey + 100, 100 * bar + 150], keys[bar][eachkey], size=[400, 80]))

        buttonList.append(Button([100 * eachkey + 100, 100 * bar + 150], keys[bar][eachkey]))


def drawAll(img, buttonList):
    for button in buttonList:
        cv2.rectangle(img, button.pos, (button.pos[0] + button.size[0], button.pos[1] + button.size[1]), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, str(button.text), (button.pos[0] + 20, button.pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
   
    return img

crop = None
state = False
thankImg = cv2.imread('/Users/khlaisuwan/Downloads/download (1).jpeg')
th, tw, _ = thankImg.shape
x = 50
y = 50
while state == False:
    status, frame  = cap.read()
    hands, img = detector.findHands(frame)
    myButton = drawAll(img, buttonList)

    if hands:
        if state == False:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                hand1 = hands[0]
                lmlist1 = hand1['lmList']
                bbox = hand1['bbox']
                
                if (x < lmlist1[8][0] < x + w) and (y < lmlist1[8][1] < y + h) and 60000 <(bbox[2] * bbox[3]) < 140000:
                    cv2.rectangle(img, button.pos, (button.pos[0] + button.size[0], button.pos[1] + button.size[1]), (250, 212, 130), cv2.FILLED)
                    cv2.putText(img, str(button.text), (button.pos[0] + 20, button.pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
                    l, _, _ = detector.findDistance(lmlist1[6][0:2], lmlist1[4][0:2], img)
                    if (l < 80) and (60000 <((bbox[2] * bbox[3])) < 140000):
                        cv2.rectangle(img, button.pos, (button.pos[0] + button.size[0], button.pos[1] + button.size[1]), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str(button.text), (button.pos[0] + 20, button.pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
                        if button.text == 'Enter':
                            state = True
                        
                        else:
                            text += button.text
                        sleep(0.25)
    cv2.rectangle(img, (0, 5), ((len(text)) * 60, 105), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, text, (10, 75),
    cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        
    
    if state == False:
        cv2.imshow('Video', img)
        cv2.waitKey(1)




    
   





