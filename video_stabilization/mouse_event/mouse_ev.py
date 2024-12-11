import cv2

# функция реакции на нажатие левой или правой кнопки мыши
def click_event(event, x, y, flags, params):

    # если нажата левая кнопка мыши
    if event == cv2.EVENT_LBUTTONDOWN:
        # выводим координаты и BGR-код точки в терминал
        print(f'Координаты точки: {x}, {y}')
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]
        print(f'BGR-код точки: {b}, {g}, {r}\n')

        # рисуем координаты точки на изображении
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'{x}, {y}', (x, y),
                    font, 1, (0, 0, 0), 2)
        cv2.imshow('image', frame)

    # если нажата правая кнопка мыши
    if event == cv2.EVENT_RBUTTONDOWN:
        # узнаём BGR-код точки и сохраняем в переменные
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]

        # выводим координаты и BGR-код точки в терминал
        print(f'Координаты точки: {x}, {y}')
        print(f'BGR-код точки: {b}, {g}, {r}\n')

        # рисуем BGR-код точки на изображении
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'{b}, {g}, {r}', (x, y),
                    font, 1, (0, 0, 0), 2)
        cv2.imshow('image', frame)


# основной сценарий
if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read(0)
        cv2.imshow('image', frame)
        # устанавливаем реакцию на действия мыши и вызываем функцию click_event
        cv2.setMouseCallback('image', click_event)
        key = cv2.waitKey(1) & 0xFF
        # проверка нажатия клавиши «q»
        if key == ord("q"):
            # если клавиша 'q' нажата, выйти из бесконечного цикла
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()