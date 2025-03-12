# https://www.youtube.com/watch?v=WgPbbWmnXJ8&t=2469s&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
# https://www.youtube.com/watch?v=neBZ6huolkg&t=242s&ab_channel=CodeInaJiffy


from ultralytics import YOLO
import cv2
# import cvzone




# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

# model =  YOLO("../Yolo_weights/yolov8n.pt")
model =  YOLO("Info_my_full/yolo11n.pt")

while True:
    success, img = cap.read()

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cv2.rectangle(img, (x1,y1), (x2,y2), (255, 0, 255), 3)



    cv2.imshow("Image", img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()