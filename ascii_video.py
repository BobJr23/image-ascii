import cv2
import numpy as np
import os
from ascii import getAscii, writeAsciiToFile
import time


input_video_path = "sunset.mp4"

cap = cv2.VideoCapture(input_video_path)

if os.path.exists(input_video_path):
    print("Video file exists")
else:
    print("Video file does not exist")

video_str = ""
while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        cv2.imshow("frame", frame)

        video_str += getAscii(frame, 128) + "p"

        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
writeAsciiToFile(video_str, "sunset.txt")
