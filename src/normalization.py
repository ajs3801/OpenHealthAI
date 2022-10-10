import mediapipe as mp
mp_pose = mp.solutions.pose

def normalization_landmark(results):
    # center_x,y,z is the center x,y,z of the left hip and right hip.
    center_x=(results.pose_landmarks.landmark[23].x+results.pose_landmarks.landmark[24].x)/2
    center_y=(results.pose_landmarks.landmark[23].y+results.pose_landmarks.landmark[24].y)/2
    center_z=(results.pose_landmarks.landmark[23].z+results.pose_landmarks.landmark[24].z)/2
    # Normalize around the center of the left and right hips
    normal=[[res.x-center_x, res.y-center_y, res.z-center_z, res.visibility] for res in results.pose_landmarks.landmark]
    return normal