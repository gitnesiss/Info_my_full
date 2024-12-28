# https://www.youtube.com/watch?v=WgPbbWmnXJ8&t=2469s&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
# https://www.youtube.com/watch?v=neBZ6huolkg&t=242s&ab_channel=CodeInaJiffy


from ultralytics import YOLO
import cv2
# import cvzone




# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

model =  YOLO("../Yolo_weights/yolov8n.pt")

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()