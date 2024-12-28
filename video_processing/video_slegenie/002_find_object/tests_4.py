from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Run inference on an image
results = model("C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_bus.jpg")  # list of 1 Results object

for result in results:
    result.show()


results = model(["C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_bus.jpg", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_zidane.jpg"])  # list of 2 Results objects

for result in results:
    result.show()

results = model(["C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\scale_2400.png", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_perekryostok.jpg"])  # list of 2 Results objects

for result in results:
    result.show()


# results = model.track("https://rutube.ru/video/9f6d2ca65e2746d36a3eac4f5bccc797/?r=plemwd", show=True)  # Tracking with default tracker