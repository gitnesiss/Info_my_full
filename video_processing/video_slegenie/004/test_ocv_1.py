import cv2
import numpy as np

def nothing(x):
  pass

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# создаём окно где будут распологаться ползунки(трекбары)
cv2.namedWindow("track")
# создаём ползунки
cv2.createTrackbar("T1", "track", 0, 255, nothing)
cv2.createTrackbar("T2", "track", 0, 255, nothing)

kernel = np.ones((5, 5))

while True:
  ret, frame = cap.read()

  # сглаживаем билатеральным фильтром основной фрейм
  biFilter = cv2.bilateralFilter(frame, 9, 75, 75)
  # переводим сглаженное изображение в серый цвет
  gray = cv2.cvtColor(biFilter, cv2.COLOR_BGR2GRAY)

  # определяем границу с помощью метода Канни
  # меняем значения беря эти значения из соответствующегои окна и соответствующего бегунка
  thresh1 = cv2.getTrackbarPos("T1", "track")
  thresh2 = cv2.getTrackbarPos("T2", "track")
  canny = cv2.Canny(gray, thresh1, thresh2)

  # делаем линии более толстыми, чтобы получить более явные контуры
  # для этого напишем ещё ядро
  dil = cv2.dilate(canny, kernel, iterations = 1)
  
  # RETR_EXTERNAL хорошо подходит для распознования контуров
  contours, h = cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  # находим самые большие контуры среди найденых в contours
  for contour in contours:
    area = cv2.contourArea(contour)
    # Если конткр больше заданного кол-ва пикселей
    if area > 10000:
      # то рисуем контур
      cv2.drawContours(frame, contour, -1, (200, 200, 0), 3)
      # Для более стабильного определения контуров нужно применить апроксимацию
      # для этого даём периметр контура
      p = cv2.arcLength(contour, True)
      # получить количество вершин и провести апроксимацию
      num = cv2.approxPolyDP(contour, 0.03 * p, True)
      # выводим количество вершин
      print(num)
      # опишем координаты и ширину с высотой прямоугольника
      x, y, w, h = cv2.boundingRect(num)
      cv2.rectangle(frame, (x, y, x+w, y+h), (0, 0, 256), 4)

  cv2.imshow("frame", frame)
#   cv2.imshow("Canny", canny)
#   cv2.imshow("Dilate", dil)

  k = cv2.waitKey(1) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()