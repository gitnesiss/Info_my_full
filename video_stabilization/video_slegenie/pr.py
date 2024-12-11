# https://www.youtube.com/watch?v=qO2nk8704Dg&ab_channel=Denis

import cv2
import numpy as np
from vidgear.gears import CamGear
#video_url = 'https://youtu.be/Tf00zM6mPT4'
video_url = 'https://www.youtube.com/watch?v=-RDeVPHipZU&ab_channel=MixedMatrixArts'
#video_url = 'https://youtu.be/MDiY0SeyfGw'
#video_url = 'https://youtu.be/gFRtAAmiFbE'

options = {
"STREAM_RESOLUTION": "720p",
"CAP_PROP_FPS": 30, # framerate 30fps
}
video = CamGear (
source=video_url,
stream_mode=True, logging=True,
**options
).start()

model_prototxt_path = 'models/caffemodel/MobileNetSSD_deploy.prototxt'
model_caffemodel_path = 'models/caffemodel/MobileNetSSD_deploy.caffemodel'
load_model = cv2.dnn.readNetFromCaffe (model_prototxt_path, model_caffemodel_path)

minimal_confidence = 0.3

categories_list = ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

# generate color for each category
np.random.seed(550000) # for better colors
colors= np.random. uniform (0, 255, size=(len(categories_list), 3))

while True:
    frame = video.read()

    if frame is None:
        break

    height, width = frame. shape[0], frame. shape[1]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (1000, 1000)), 0.007, (1000, 1000), 130) # blob (Binary Large Object)
    
    load_model.setInput (blob)
    detected_objects = load_model.forward()
    
    for i in range(detected_objects.shape[2]):
        confidence = detected_objects[0][0][1][2]
        
        if confidence > minimal_confidence:
            category_index = int(detected_objects [0, 0, 1, 1])
            
            upper_left_x = int(detected_objects [0, 0, i, 3] * width)
            upper_left_y = int(detected_objects [0, 0, i, 4] * height)
            lower_right_x = int(detected_objects [0, 0, 1, 5] * width)
            lower_right_y = int(detected_objects [0, 0, 1, 6] * height)
            
            # draw rectangle
            cv2.rectangle(frame, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors [category_index], 3)
            
            # put text in upper part of rectangle
            # format confidence = f'{confidence:.2f}'
            format_confidence = '100' if round (confidence, 1) == 1.0 else f'{confidence: .2f}'.replace('0.','')
            detected_obj_text = f'{categories_list [category_index]}: {format_confidence}%'
            cv2.putText(frame, detected_obj_text, (upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors [category_index], 2)
    cv2.imshow('Detected Objects', frame)
    # press Esc to exit
    # if cv2.waitKey(1) == 27: # faster
        # break
    if cv2.waitKey(33) == 27: # slower .......
        break
video.stop()
cv2.destroyAllWindows()





# import cv2

# # функция реакции на нажатие левой или правой кнопки мыши
# def click_event(event, x, y, flags, params):

#     # если нажата левая кнопка мыши
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # выводим координаты и BGR-код точки в терминал
#         print(f'Координаты точки: {x}, {y}')
#         b = img[y, x, 0]
#         g = img[y, x, 1]
#         r = img[y, x, 2]
#         print(f'BGR-код точки: {b}, {g}, {r}\n')

#         # рисуем координаты точки на изображении
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, f'{x}, {y}', (x, y),
#                     font, 1, (0, 0, 0), 2)
#         cv2.imshow('image', img)

#     # если нажата правая кнопка мыши
#     if event == cv2.EVENT_RBUTTONDOWN:
#         # узнаём BGR-код точки и сохраняем в переменные
#         b = img[y, x, 0]
#         g = img[y, x, 1]
#         r = img[y, x, 2]

#         # выводим координаты и BGR-код точки в терминал
#         print(f'Координаты точки: {x}, {y}')
#         print(f'BGR-код точки: {b}, {g}, {r}\n')

#         # рисуем BGR-код точки на изображении
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, f'{b}, {g}, {r}', (x, y),
#                     font, 1, (0, 0, 0), 2)
#         cv2.imshow('image', img)


# # основной сценарий
# if __name__ == "__main__":
#     img = cv2.imread('py_logo.png', 1)
#     cv2.imshow('image', img)
#     # устанавливаем реакцию на действия мыши и вызываем функцию click_event
#     cv2.setMouseCallback('image', click_event)
#     cv2.waitKey(0)







# import cv2
# import numpy as np

# img = cv2.imread("C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\py_logo.png", -1)
# # cv2.namedWindow("image_logo", cv2.WINDOW_AUTOSIZE)
# # cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
