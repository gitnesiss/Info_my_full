# Программа обучает модель

from ultralytics import YOLO

# Инициализация модели YOLO11n из файла конфигурации YAML
# model = YOLO("model.yaml")

# Если доступна предварительно обученная модель, используйте ее.
# model = YOLO("model.pt")
model = YOLO("C:\\code\\tests\\ocv_env\\ocv_yolo_test\\yolo11n.pt")



# Отображение информации о модели
model.info()

# Обучите модель, используя набор данных COCO8 в течение 100 эпох.
model.train(data="coco8.yaml", epochs=100)

# Оцените эффективность модели на проверочном наборе
results = model.val()



# Выполнить обнаружение объектов на изображении с использованием модели
results = model("C:\\code\\tests\\ocv_env\\ocv_yolo_test\\madia_crasswalk_orig.jpg")

# Visualize the results
for result in results:
    result.show()

## Export the model to ONNX format
# success = model.export(format="onnx")