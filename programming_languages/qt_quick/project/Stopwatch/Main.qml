import QtQuick
import QtQuick.Controls
import QtQuick.Window
import Stopwatch 1.0  // Импортируем наш C++ модуль. Позволяет определять
                      // Main.qml экземпляр класса Stopwatch. Можно закоментить,
                      // но qml не будет понимать Stopwatch, при этом проект
                      // будет собираться потому что он прописан в CMakeList.txt.

Window {
    width: 640      // Ширина окна
    height: 480     // Высота окна
    minimumWidth: 400
    minimumHeight: 300
    visible: true   // Делаем окно видимым
    // title: "Секундомер"
    title: qsTr("Секундомер")   // Заголовок окна
    color: "#f0f0f0"            // Цвет фона (светло-серый)

    // Создаем экземпляр секундомера Stopwatch (наш C++ класс)
    Stopwatch {
        id: stopwatch  // Идентификатор для доступа к свойствам и методам

        // Автоматический старт при создании компонента
        Component.onCompleted: {
            console.log("Секундомер создан. Запускаем...")
            startStop()
        }
    }

    // Вертикальный контейнер для элементов
    Column {
        anchors.centerIn: parent  // Центрируем по центру окна
        spacing: 40               // Расстояние между элементами

        // Текстовый элемент для отображения времени
        Text {
            id: timeDisplay
            text: stopwatch.time    // Привязываем текст к свойству time из C++
            font {
                family: "Monospace" // Моноширинный шрифт для ровного отображения цифр
                pixelSize: 48
                bold: true
            }
            color: "#333"
        }

        // Кнопка "Стоп/Продолжить"
        Button {
            id: controlButton
            text: stopwatch.running ? "Стоп" : "Продолжить" // Текст зависит от состояния
            onClicked: stopwatch.startStop()                // Обработчик клика. При нажатии вызываем метод startStop

            // Стилизация кнопки. Настройки внешнего вида
            width: 200
            height: 50
            font.pixelSize: 20
            background: Rectangle {
                color: parent.down ? "#d0d0d0" : "#e0e0e0"  // Изменение цвета при нажатии
                radius: 5
                border.color: "#999"
            }
            anchors {
                horizontalCenter: parent.horizontalCenter
            }
        }

        // Кнопка "Сброс"
        Button {
            id: resetButton
            text: "Сброс"
            onClicked: stopwatch.reset()    // При нажатии вызываем reset

            width: 200
            height: 50
            font.pixelSize: 20
            background: Rectangle {
                color: parent.down ? "#d0d0d0" : "#e0e0e0"
                radius: 5
                border.color: "#999"
            }
            anchors {
                horizontalCenter: parent.horizontalCenter
            }

            // Анимация нажатия
            Behavior on scale {
                NumberAnimation { duration: 100 }
            }
        }
    }

    // Статусная строка
    Text {
        id: statusText
        anchors {
            bottom: parent.bottom
            horizontalCenter: parent.horizontalCenter
            margins: 10
        }
        text: stopwatch.running ? qsTr("Секундомер работает") : qsTr("Секундомер остановлен")
        font.italic: true
        color: "#666"
    }

    // Обработчик изменения состояния
    Connections {
        target: stopwatch
        function onRunningChanged() {
            console.log("Состояние изменено:", stopwatch.running ? "работает" : "остановлен")
        }
    }
}
