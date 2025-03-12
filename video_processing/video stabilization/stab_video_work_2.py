# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
from vidgear.gears import VideoGear
import numpy as np
import cv2
import datetime
import os

# open any valid video stream with stabilization enabled(`stabilize = True`)
stream_stab = VideoGear(source=0, stabilize=True, backend=cv2.CAP_DSHOW).start()

stream_not_stab = VideoGear(source=0, backend=cv2.CAP_DSHOW).start()

help = False
help_on = "help:  ON"
help_off = "help: OFF"
help_text = help_off

stab = True
stab_on = "Stab:  ON"
stab_off = "Stab: OFF"
stab_text = stab_on

rec = False
rec_on = "REC:  ON"
rec_off = "REC: OFF"
rec_text = rec_off


# Определяем текущую дату в формате год-месяц-день
path_date = datetime.datetime.today().strftime('%Y-%m-%d')
# Создаём переменную где формируем имя пути куда будет записываться видео
path_video_dir = (f"C:\\video\\{path_date}")
# Создание директории куда записывать видеофайл
# Постараться создать файл
try:
    os.mkdir(path_video_dir)
    print(f"Директория {path_video_dir} создана.")
# если такая директория существует, то пропускаем это действие
except OSError:
    print(f"Директория {path_video_dir} уже существует.")
    pass

numberVideo = 1
str_numberVideo = str(numberVideo).zfill(4)
print("C:\\video\\{}\\{}_stab_video_{}_{}.mp4".format(path_date, datetime.datetime.today().strftime('%Y-%m-%d'), str_numberVideo, datetime.datetime.today().strftime('%H-%M-%S')))
path_video_save = "C:\\video\\{}\\{}_stab_video_{}_{}.mp4".format(path_date, datetime.datetime.today().strftime('%Y-%m-%d'), str_numberVideo, datetime.datetime.today().strftime('%H-%M-%S'))

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output = f"{path_video_save}")



# loop over
while True:
    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if None-type
    if frame_stab is None:
        break

    frame_not_stab = stream_not_stab.read()

    # {do something with the frame here}
    if stab == True:
        stab_text = stab_on
        image = np.ascontiguousarray(frame_stab, dtype=np.uint8)
        stab_text_r = 0
        stab_text_b = 0
        stab_text_g = 255
    else:
        stab_text = stab_off
        # добавляю слой для возможности вставить текст. Если этого не сделать программа не будет работать
        image = np.ascontiguousarray(frame_not_stab, dtype=np.uint8)
        stab_text_r = 255
        stab_text_b = 0
        stab_text_g = 0
    
    if rec == True:
        rec_text = rec_on
        rec_text_r = 0
        rec_text_b = 0
        rec_text_g = 255
    else:
        rec_text = rec_off
        rec_text_r = 255
        rec_text_b = 0
        rec_text_g = 0

    # Вывод времени и даты на фрейм
    # Русский стиль
    date="Time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %a"))
    # Американский стиль
    # date="Time: {}".format(datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"))
    # Вывожу в консоль дату и время
    # print(date)
    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, date, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1) 

    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, stab_text, (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (stab_text_b, stab_text_g, stab_text_r), 2,)
    
    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, rec_text, (540, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (rec_text_b, rec_text_g, rec_text_r), 2,)
    
    if help == True:
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "q - exit", (540, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "s - stab", (540, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "r - rec", (540, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
    else:
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "\"h\" help", (540, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1,)

    # Запись кадра в файл
    if rec == True:
        writer.write(image)

    # Show output window
    cv2.imshow("Stabilized Output", image)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("r"):
        rec = not rec
        print(f"rec:  {rec}")
    
    if key == ord("s"):
        stab = not stab
        print(f"stab: {stab}")

    if key == ord("h"):
        help = not help
        print(f"help: {stab}")
    
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close streams
stream_stab.stop()
