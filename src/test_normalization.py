import cv2
import numpy as np
import mediapipe as mp
from normalization import normalization_landmark
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("rose.jpg")
with mp_pose.Pose(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as pose:
    success, image = cap.read()
    results = pose.process(image)

    print(normalization_landmark(results))
cap.release()