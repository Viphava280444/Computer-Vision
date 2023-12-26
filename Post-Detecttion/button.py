import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

class Button():
    def __init__(self, pos, text, size=[80, 80]) -> None:
        self.pos = pos
        self.size = size
        self.text = text

  