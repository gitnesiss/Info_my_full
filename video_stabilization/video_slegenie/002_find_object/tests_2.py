from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Perform object detection on an image
results = model("https://ultralytics.com/images/bus.jpg")

# Visualize the results
for result in results:
    result.show()




# from ultralytics import YOLO

# # Load a model
# model = YOLO("yolo11n.pt")  # load an official detection model
# model = YOLO("yolo11n-seg.pt")  # load an official segmentation model
# model = YOLO("C:\\code\\runs\\detect\\train7\\weights\\best.pt")  # load a custom model

# # Track with the model
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")





# import cv2
# from PIL import Image

# from ultralytics import YOLO

# model = YOLO("model.pt")
# # принимает все форматы — image/dir/Path/URL/video/PIL/ndarray. 0 для веб-камеры
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True)  # Отображение предикат. Принимает все аргументы прогноза YOLO

# # from PIL
# im1 = Image.open("bus.jpg")
# results = model.predict(source=im1, save=True)  # save plotted images

# # from ndarray
# im2 = cv2.imread("bus.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])