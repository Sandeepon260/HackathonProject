import cv2
import mediapipe as mp
import numpy
import poseModule as pm


detector = pm.poseDetector(mode=True)

left = [11, 23, 25, 27, 29, 31]
right = [12, 24, 26, 28, 30, 32]
img = cv2.imread("test2.png")
detector.findPose(img, draw=False)
lmlist, img = detector.findPosition(img, draw=False)
angle, img = detector.findAngle(img, right[0], right[1], right[2])
angle2, img = detector.findAngle(img, right[2], right[3], right[4])
angle2, img = detector.findAngle(img, right[4], right[5], right[5])
result = detector.angle_from_horizontal(right[0], right[1])

print(result)
print(result2)
print(result3)
# print(lmlist)

# 1. Back Angle
# 2. Lower than knee
# 3. Knee over foot

# cv2.imshow("", img)
# cv2.waitKey()
