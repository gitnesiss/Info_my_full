# # import required libraries
# from vidgear.gears import CamGear
# import cv2

# # set desired quality as 720p
# # options = {"STREAM_RESOLUTION": "720p"}

# # Add any desire Video URL as input source
# # for e.g https://vimeo.com/151666798
# # and enable Stream Mode (`stream_mode = True`)
# stream = CamGear(
#     source='rtsp://admin:123456@192.168.11.174:554/stream0',
#     stream_mode=False,
#     logging=True,
#     # **options
# ).start()

# # loop over
# while True:

#     # read frames from stream
#     frame = stream.read()

#     # check for frame if Nonetype
#     if frame is None:
#         break

#     # {do something with the frame here}

#     # Show output window
#     cv2.imshow("Output", frame)

#     # check for 'q' key if pressed
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord("q"):
#         break

# # close output window
# cv2.destroyAllWindows()

# # safely close video stream
# stream.stop()





from vidgear.gears import CamGear
import cv2
import datetime
import time


class Reconnecting_CamGear:
    def __init__(self, cam_address, reset_attempts=50, reset_delay=5):
        self.cam_address = cam_address
        self.reset_attempts = reset_attempts
        self.reset_delay = reset_delay
        self.source = CamGear(source=self.cam_address).start()
        self.running = True

    def read(self):
        if self.source is None:
            return None
        if self.running and self.reset_attempts > 0:
            frame = self.source.read()
            if frame is None:
                self.source.stop()
                self.reset_attempts -= 1
                print(
                    "Re-connection Attempt-{} occured at time:{}".format(
                        str(self.reset_attempts),
                        datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S%p"),
                    )
                )
                time.sleep(self.reset_delay)
                self.source = CamGear(source=self.cam_address).start()
                # return previous frame
                return self.frame
            else:
                self.frame = frame
                return frame
        else:
            return None

    def stop(self):
        self.running = False
        self.reset_attempts = 0
        self.frame = None
        if not self.source is None:
            self.source.stop()


if __name__ == "__main__":
    # open any valid video stream
    stream = Reconnecting_CamGear(
        cam_address="rtsp://admin:123456@192.168.11.174:554/stream0",
        reset_attempts=20,
        reset_delay=5,
    )

    # loop over
    while True:

        # read frames from stream
        frame = stream.read()

        # check for frame if None-type
        if frame is None:
            break

        # {do something with the frame here}

        # Show output window
        cv2.imshow("Output", frame)

        # check for 'q' key if pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # close output window
    cv2.destroyAllWindows()

    # safely close video stream
    stream.stop()