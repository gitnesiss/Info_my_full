# from ultralytics import YOLO

# # Load a pretrained YOLO11n model
# model = YOLO("yolo11n.pt")

# # Run inference on an image
# results = model("C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\bus.jpg")  # results list

# # View results
# for r in results:
#     print(r.boxes)  # print the Boxes object containing the detection bounding boxes

    
    
    


from ultralytics import YOLO

# Load a pretrained YOLO11n-pose Pose model
model = YOLO("yolo11n-pose.pt")

# Run inference on an image
results = model("C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_bus.jpg")  # results list

# View results
for r in results:
    print(r.keypoints)  # print the Keypoints object containing the detected keypoints