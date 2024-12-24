# Программа обучает модель

from ultralytics import YOLO

# Инициализация модели YOLO11n из файла конфигурации YAML
# model = YOLO("model.yaml")

# Если доступна предварительно обученная модель, используйте ее.
# model = YOLO("model.pt")
# model = YOLO("C:\\code\\tests\\ocv_env\\ocv_yolo_test\\yolo11n.pt")
model = YOLO("yolo11n.pt")




##### Этот кусочек кода можно отключать чтобы использовать модель с обучением #####

# Отображение информации о модели
model.info()

# Обучите модель, используя набор данных COCO8 в течение 100 эпох.
model.train(data="coco8.yaml", epochs=100)

# Оцените эффективность модели на проверочном наборе
results = model.val()

##### Этот кусочек кода можно отключать чтобы использовать модель с обучением #####




# Выполнить обнаружение объектов на изображении с использованием модели
# В VSC скопировать путь из дерева проекта до файла
results = model("C:\code\Info_my_full\\video_stabilization\\video_slegenie\images\madia_crasswalk_orig.jpg")

# Показать результат
for result in results:
    result.show()

## Экспортировать модель в формат ONNX
# success = model.export(format="onnx")