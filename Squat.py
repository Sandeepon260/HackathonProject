import cv2
import mediapipe as mp
import numpy
import poseModule as pm

detector = pm.poseDetector(mode=True)

img = cv2.imread("test2.png")
detector.findPose(img)
lmlist, img = detector.findPosition(img, draw=False)

print(lmlist)


cv2.imshow("", img)
cv2.waitKey()
