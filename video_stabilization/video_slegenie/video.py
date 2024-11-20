import cv2
# Загрузка видеопотока с камеры
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0, cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1536) 
# Создание объекта алгоритма оптического потока
# optical_flow = cv2.DualTVL1OpticalFlow_create()
# optical_flow = cv2.optical_flow = cv2.optflow.DualTVL1OpticalFlow_create()
optical_flow = cv2.optflow.DualTVL1OpticalFlow_create()
# Чтение первого кадра видеопотока
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
# Основной цикл для обработки видеопотока
while True:
    # Чтение текущего кадра
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Расчет оптического потока
    flow = optical_flow.calc(prev_gray, gray, None)
    # Отрисовка оптического потока на кадре
    flow_vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    flow_vis = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # current_opt_flow = optical_flow.calc(prvs, next, None)
    cv2.imshow('Optical Flow', flow_vis)
    # Обновление предыдущего кадра
    prev_gray = gray.copy()
    # Выход из цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()





# import cv2
# # Загрузка изображения
# # image = cv2.imread("2024-05-30_123026.png", -1)
# image = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\scale_2400.png', 1)
# # Создание объекта детектора ORB
# orb = cv2.ORB_create()
# # Поиск ключевых точек и их описаний на изображении
# keypoints, descriptors = orb.detectAndCompute(image, None)
# # Рисование найденных ключевых точек на изображении
# image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)
# # image_with_keypoints = cv2.drawKeypoints(image, keypoints, 0, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# # Вывод изображения с ключевыми точками
# cv2.imshow('Image with Keypoints', image_with_keypoints)  # Вывод изображения с ключевыми точками
# # cv2.imshow('Image with Keypoints', image)  # Вывод оригинального изображения
# cv2.waitKey(0)  
# cv2.destroyAllWindows()





# import cv2
# import numpy as np
# # img = cv2.imread("py_logo.png")
# img = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\2024-05-30_123026.png', 1)
# cv2.namedWindow("image_logo", cv2.WINDOW_AUTOSIZE)
# # cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL)
# cv2.imshow("image_logo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\py_logo.png', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()