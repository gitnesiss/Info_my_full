# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import numpy as np
import cv2

# open any valid video stream with stabilization enabled(`stabilize = True`)
stream_stab = VideoGear(source=0, stabilize=True, backend=cv2.CAP_DSHOW).start()

# open same stream without stabilization for comparison
stream_org = VideoGear(source=0, backend=cv2.CAP_DSHOW).start()

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output = 'Save_video_duo_cam.mp4') 

# loop over
while True:

    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if Nonetype
    if frame_stab is None:
        break

    # read un-stabilized frame
    frame_org = stream_org.read()

    # concatenate both frames
    output_frame = np.concatenate((frame_org, frame_stab), axis=1)

    # put text over concatenated frame
    cv2.putText(
        output_frame, "Before", (10, output_frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
    )
    cv2.putText(
        output_frame, "After", (output_frame.shape[1] // 2 + 10, output_frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
    )

    # Запись кадра в файл
    writer.write(output_frame)

    # Show output window
    cv2.imshow("Stabilized Frame", output_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close both video streams
stream_org.stop()
stream_stab.stop()