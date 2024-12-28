from threading import Thread

from ultralytics import YOLO


def thread_safe_predict(model, image_path):
    """Performs thread-safe prediction on an image using a locally instantiated YOLO model."""
    model = YOLO(model)
    results = model.predict(image_path)
    # Process results


# Starting threads that each have their own model instance
Thread(target=thread_safe_predict, args=("yolo11n.pt", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_bus.jpg")).start()
Thread(target=thread_safe_predict, args=("yolo11n.pt", "C:\\code\\Info_my_full\\video_processing\\video_slegenie\\images\\media_zidane.jpg")).start()