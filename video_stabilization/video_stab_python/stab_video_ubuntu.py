## https://abhitronix.github.io/vidgear/v0.3.3-stable/gears/videogear/params/#source

from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import cv2
import datetime
import os
import numpy as np


stream_stab = VideoGear(source=0, stabilize = True).start()

vis_help = False
vis_help_on = "help:  ON"
vis_help_off = "help: OFF"
vis_help_text = vis_help_off

vis_stab = True
vis_stab_on = "Stab:  ON"
vis_stab_off = "Stab: OFF"
vis_stab_text = vis_stab_on

vis_rec = False
vis_rec_on = "REC:  ON"
vis_rec_off = "REC: OFF"
vis_rec_text = vis_rec_off

vis_date = True
vis_date_on = "Date:  ON"
vis_date_off = "Date: OFF"
vis_date_text = vis_date_on


# Определяем текущую дату в формате год-месяц-день
path_date = datetime.datetime.today().strftime('%Y-%m-%d')
# Создаём переменную где формируем имя пути куда будет записываться видео
# path_video_dir = "home/roman/code/video/{}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# Создание директории куда записывать видеофайл
# Постараться создать файл
try:
    os.mkdir(path_date)
    print(f"Директория {path_date} создана.")
# если такая директория существует, то пропускаем это действие
except OSError:
    print(f"Директория {path_date} уже существует.")
    pass

numberVideo = 1
str_numberVideo = str(numberVideo).zfill(4)
print("{}/{}_stab_video_{}_{}.mp4".format(path_date, datetime.datetime.today().strftime('%Y-%m-%d'), str_numberVideo, datetime.datetime.today().strftime('%H-%M-%S')))
path_video_save = "{}/{}_stab_video_{}_{}.mp4".format(path_date, datetime.datetime.today().strftime('%Y-%m-%d'), str_numberVideo, datetime.datetime.today().strftime('%H-%M-%S'))

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output = f"{path_video_save}")



# Бесконечный цикл
# loop over
while True:
    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if None-type
    if frame_stab is None:
        break

    # {do something with the frame here}
    if vis_stab == True:
        stab_text = vis_stab_on
        image = np.ascontiguousarray(frame_stab, dtype=np.uint8)
        stab_text_r = 0
        stab_text_b = 0
        stab_text_g = 255
    else:
        stab_text = vis_stab_off
        # добавляю слой для возможности вставить текст. Если этого не сделать программа не будет работать
        image = np.ascontiguousarray(frame_stab, dtype=np.uint8)
        stab_text_r = 255
        stab_text_b = 0
        stab_text_g = 0
    
    
    if vis_rec == True:
        rec_text = vis_rec_on
        rec_text_r = 0
        rec_text_b = 0
        rec_text_g = 255
    else:
        rec_text = vis_rec_off
        rec_text_r = 255
        rec_text_b = 0
        rec_text_g = 0
    

    date="Time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    # Вывожу в консоль дату и время
    # print(date)
    
    if vis_date == True:
        cv2.putText(image, date, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1)

    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, stab_text, (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (stab_text_b, stab_text_g, stab_text_r), 2,)
    
    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, rec_text, (540, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (rec_text_b, rec_text_g, rec_text_r), 2,)

    if vis_help == True:
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "q - exit", (540, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "d - date", (540, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "r - rec", (540, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "s - stab", (540, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2,)
    else:
        # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
        cv2.putText(image, "\"h\" help", (540, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1,)

    # Запись кадра в файл
    if vis_rec == True:
        writer.write(image)

    # Show output window
    cv2.imshow("Stabilized Output", image)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("r"):
        vis_rec = not vis_rec
        print(f"rec:  {vis_rec}")
    
    if key == ord("s"):
        vis_stab = not vis_stab
        if vis_stab == True:
            stream_stab.stop()
            stream_stab = VideoGear(source=0, stabilize = True).start()
        else:
            stream_stab.stop()
            stream_stab = VideoGear(source=0, stabilize = False).start()
        print(f"stab: {vis_stab}")

    if key == ord("h"):
        vis_help = not vis_help
        print(f"help: {vis_help}")
    
    if key == ord("d"):
        vis_date = not vis_date
        print(f"date: {vis_date}")
    
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close streams
stream_stab.stop()