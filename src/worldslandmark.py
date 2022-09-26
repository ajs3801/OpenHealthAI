import cv2
import numpy as np
import mediapipe as mp
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("rose.jpg")
with mp_pose.Pose(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as pose:
    success, image = cap.read()
    results = pose.process(image)

    center_x=(results.pose_world_landmarks.landmark[23].x+results.pose_world_landmarks.landmark[24].x)/2
    center_y=(results.pose_world_landmarks.landmark[23].y+results.pose_world_landmarks.landmark[24].y)/2
    center_z=(results.pose_world_landmarks.landmark[23].z+results.pose_world_landmarks.landmark[24].z)/2
    normal=np.array([[res.x+center_x, res.y+center_y, res.z+center_z, res.visibility] for res in results.pose_world_landmarks.landmark]) if results.pose_world_landmarks else np.zeros(33*4)
    print(normal)
cap.release()