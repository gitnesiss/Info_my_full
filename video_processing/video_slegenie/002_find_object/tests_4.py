# from ultralytics import YOLO

# # Load an official or custom model
# # model = YOLO("yolo11n.pt")  # Load an official Detect model
# # model = YOLO("yolo11n-seg.pt")  # Load an official Segment model
# model = YOLO("yolo11n-pose.pt")  # Load an official Pose model
# # model = YOLO("path/to/best.pt")  # Load a custom trained model

# # Perform tracking with the model
# # results = model.track("https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker
# results = model.track(source=0, show=True)  # Tracking with default tracker
# # results = model.track("https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # with ByteTrack

from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Run inference on an image
results = model("C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\bus.jpg")  # list of 1 Results object

for result in results:
    result.show()


results = model(["C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\bus.jpg", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\zidane.jpg"])  # list of 2 Results objects

for result in results:
    result.show()

results = model(["C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\scale_2400.png", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_perekryostok.jpg"])  # list of 2 Results objects

for result in results:
    result.show()