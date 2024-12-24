# import required libraries
from vidgear.gears.stabilizer import Stabilizer
from vidgear.gears import CamGear
import cv2

# Открыть прямую трансляцию видео на веб-камере на первом индексном устройстве (т.е. 0)
stream = CamGear(source=0).start()

# инициировать объект стабилизатора с параметрами по умолчанию
stab = Stabilizer()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # send current frame to stabilizer for processing
    stabilized_frame = stab.stabilize(frame)

    # wait for stabilizer which still be initializing
    if stabilized_frame is None:
        continue

    # {do something with the stabilized frame here}

    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(frame, "Stabilizing: on", (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2) 
    
    # Show output window
    cv2.imshow("Output Stabilized Frame", stabilized_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# clear stabilizer resources
stab.clean()

# safely close video stream
stream.stop()





# # import required libraries
# from vidgear.gears import VideoGear
# import numpy as np
# import cv2

# # open any valid video stream with stabilization enabled(`stabilize = True`)
# stream_stab = VideoGear(source="test.mp4", stabilize=True).start()

# # open same stream without stabilization for comparison
# stream_org = VideoGear(source="test.mp4").start()

# # loop over
# while True:

#     # read stabilized frames
#     frame_stab = stream_stab.read()

#     # check for stabilized frame if Nonetype
#     if frame_stab is None:
#         break

#     # read un-stabilized frame
#     frame_org = stream_org.read()

#     # concatenate both frames
#     output_frame = np.concatenate((frame_org, frame_stab), axis=1)

#     # put text over concatenated frame
#     cv2.putText(
#         output_frame,
#         "Before",
#         (10, output_frame.shape[0] - 10),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.6,
#         (0, 255, 0),
#         2,
#     )
#     cv2.putText(
#         output_frame,
#         "After",
#         (output_frame.shape[1] // 2 + 10, output_frame.shape[0] - 10),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.6,
#         (0, 255, 0),
#         2,
#     )

#     # Show output window
#     cv2.imshow("Stabilized Frame", output_frame)

#     # check for 'q' key if pressed
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord("q"):
#         break

# # close output window
# cv2.destroyAllWindows()

# # safely close both video streams
# stream_org.stop()
# stream_stab.stop()