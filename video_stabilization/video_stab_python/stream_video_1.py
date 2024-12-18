import cv2
import os
import numpy as np
from vidgear.gears import VideoGear


cap = cv2.VideoCapture("rtsp://admin:123456@192.168.11.174:554/stream0")

cv2.namedWindow("foo", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("foo", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

w = 2592
h = 1944
w_goal = 1920  # целевая ширина кадра
h_goal = 1080  # целевая высота кадра
h_monitor = h/h_goal  # 1944 / 1080 = 1.8 - коэф. текущего расширения: отношение требуемой высоты к высоте картинки приходящей с камеры расширения
# h_monitor = 2
h_crop_y_1 = int((h-h_goal)/2)      #432
h_crop_y_2 = int(h-((h-h_goal)/2))  #1512          1512-432 = 1080
w_crop_x_1 = int((w-w_goal)/2)      #336
w_crop_x_2 = int(w-((w-w_goal)/2))  #2256          2256-336 = 1920


crop_width = int(w / h_monitor)     #1440
crop_height = int(h / h_monitor)    #1080
print(crop_width)
print(crop_height)

crop = False
crop_on = "crop:  ON"
crop_off = "crop: OFF"
crop_text = crop_off

while(cap.isOpened()):
    ret, frame = cap.read()

    if crop == True:
        # вырезаем из фрагмента с расширением 2592*1944 фрагмент 1920*1080
        frame_ready = frame[h_crop_y_1:h_crop_y_2, w_crop_x_1:w_crop_x_2] # frame_crop (y0:y1, x0:x1) - вырезаем нужный фрагмент картинки
        cv2.putText(frame_ready, "c - crop", (w_goal - 100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 134, 54), 2,)
    else:
        # изменение размера картинки
        frame_ready = cv2.resize(frame, (crop_width, crop_height), cv2.INTER_NEAREST)
        cv2.putText(frame_ready, "c - crop", (crop_width - 100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 134, 54), 2,)

    cv2.imshow('frame', frame_ready)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        crop = not crop
        print(f"crop: {crop}")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
