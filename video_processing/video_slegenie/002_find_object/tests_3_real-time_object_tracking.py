from ultralytics import YOLO

# Load a pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
# results = model.track(source="C:\Video\GX010165.MP4")
# results = model.track(source="C:\Video\GX010165.MP4", conf=0.3, iou=0.5, show=True)
results = model.track(source="C:\\Video\\2024-11-05 Испытания катапульты. Запуск с катапульты\\1.mp4", conf=0.3, iou=0.5, show=True)
# results = model.track(source="C:\\Video\\2024-11-05 Испытания катапульты. Запуск с катапульты\\video_2023-11-29_21-58-27.mp4", conf=0.3, iou=0.5, show=True)

# # Показать результат
# for result in results:
#     result.show()