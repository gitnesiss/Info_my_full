from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n-obb.pt")

# Run inference on an image
results = model("C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_boats.jpg")  # results list

# View results
for r in results:
    print(r.obb)  # print the OBB object containing the oriented detection bounding boxes

# Visualize the results
for result in results:
    result.show()