import cv2
import os
import numpy as np
from vidgear.gears import VideoGear
cap = cv2.VideoCapture("rtsp://admin:123456@192.168.11.174:554/stream0")

w = 2592
h = 1944
h_monitor = h/1080  # 1944 / 1080 = 1.8
# h_monitor = 1

# h_crop_y_1 = 432
# h_crop_y_2 = 1512
# w_crop_x_1 = 0
# w_crop_x_2 = 2592

crop = False
crop_on = "crop:  ON"
crop_off = "crop: OFF"
crop_text = crop_off

while(cap.isOpened()):
    ret, frame = cap.read()

    if crop == True:
        frame_resize = frame[432:1512, 0:2592]
        frame_crop = frame_resize
        cv2.imshow('frame', frame_crop)
    else:
        frame = cv2.resize(frame, (int(w / h_monitor), int(h / h_monitor)), cv2.INTER_NEAREST)
        cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        crop = not crop
        print(f"crop: {crop}")

    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
