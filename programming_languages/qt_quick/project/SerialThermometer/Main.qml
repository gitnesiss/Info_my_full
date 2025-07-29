// import QtQuick

// Window {
//     width: 640
//     height: 480
//     visible: true
//     title: qsTr("Hello World")
// }

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import SerialThermometer 1.0

ApplicationWindow {
    id: mainWindow
    width: 800
    height: 600
    visible: true
    title: qsTr("Умный термометр")

    // SerialReader {
    //     id: serialReader
    //     onErrorOccurred: (message) => errorDialog.show(message)
    // }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 20

        // Панель управления
        RowLayout {
            Layout.fillWidth: true

            ComboBox {
                id: portComboBox
                Layout.fillWidth: true
                model: serialReader.availablePorts()
                displayText: currentIndex === -1 ? "Выберите порт" : currentText
            }

            Button {
                text: "Обновить"
                onClicked: portComboBox.model = serialReader.availablePorts()
            }

            Button {
                text: serialReader.connected ? "Отключить" : "Подключить"
                enabled: portComboBox.currentIndex !== -1
                onClicked: {
                    if (serialReader.connected) {
                        serialReader.disconnectDevice()
                    } else {
                        serialReader.connectDevice(portComboBox.currentText)
                    }
                }
            }
        }

        // Индикаторы температуры и влажности
        GridLayout {
            columns: 2
            Layout.fillWidth: true

            // Температура
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 200
                color: "#f0f8ff"
                radius: 10
                border.color: "#d0e0f0"

                ColumnLayout {
                    anchors.centerIn: parent
                    spacing: 10

                    Label {
                        text: qsTr("Температура")
                        font.bold: true
                        font.pointSize: 16
                        Layout.alignment: Qt.AlignHCenter
                    }

                    Label {
                        text: serialReader.temperature.toFixed(1) + "°C"
                        font.pointSize: 32
                        color: serialReader.temperature > 30 ? "#e74c3c" : "#3498db"
                        Layout.alignment: Qt.AlignHCenter
                    }
                }
            }

            // Влажность
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 200
                color: "#f0f8ff"
                radius: 10
                border.color: "#d0e0f0"

                ColumnLayout {
                    anchors.centerIn: parent
                    spacing: 10

                    Label {
                        text: qsTr("Влажность")
                        font.bold: true
                        font.pointSize: 16
                        Layout.alignment: Qt.AlignHCenter
                    }

                    Label {
                        text: serialReader.humidity.toFixed(1) + "%"
                        font.pointSize: 32
                        color: "#2ecc71"
                        Layout.alignment: Qt.AlignHCenter
                    }
                }
            }
        }

        // График истории
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: "#f8f8f8"
            border.color: "#d0d0d0"
            radius: 5

            Canvas {
                id: chartCanvas
                anchors.fill: parent
                anchors.margins: 10

                property var tempData: []
                property var humData: []
                property int maxPoints: 50

                onPaint: {
                    var ctx = getContext("2d");
                    ctx.clearRect(0, 0, width, height);

                    // Рисуем сетку
                    ctx.strokeStyle = "#e0e0e0";
                    ctx.lineWidth = 1;

                    // Горизонтальные линии
                    for (var y = 0; y <= height; y += height / 4) {
                        ctx.beginPath();
                        ctx.moveTo(0, y);
                        ctx.lineTo(width, y);
                        ctx.stroke();
                    }

                    // Рисуем данные температуры
                    if (tempData.length > 1) {
                        ctx.strokeStyle = "#e74c3c";
                        ctx.lineWidth = 2;
                        ctx.beginPath();

                        for (var i = 0; i < tempData.length; i++) {
                            var x = i * (width / (maxPoints - 1));
                            var y = height - (tempData[i] * height / 50); // 50°C max

                            if (i === 0) {
                                ctx.moveTo(x, y);
                            } else {
                                ctx.lineTo(x, y);
                            }
                        }

                        ctx.stroke();
                    }

                    // Рисуем данные влажности
                    if (humData.length > 1) {
                        ctx.strokeStyle = "#3498db";
                        ctx.lineWidth = 2;
                        ctx.beginPath();

                        for (var j = 0; j < humData.length; j++) {
                            var x = j * (width / (maxPoints - 1));
                            var y = height - (humData[j] * height / 100);

                            if (j === 0) {
                                ctx.moveTo(x, y);
                            } else {
                                ctx.lineTo(x, y);
                            }
                        }

                        ctx.stroke();
                    }
                }
            }

            // Обновление графика при получении новых данных
            Connections {
                target: serialReader
                function onDataReceived() {
                    // Добавляем новые точки
                    chartCanvas.tempData.push(serialReader.temperature);
                    chartCanvas.humData.push(serialReader.humidity);

                    // Ограничиваем количество точек
                    if (chartCanvas.tempData.length > chartCanvas.maxPoints) {
                        chartCanvas.tempData.shift();
                        chartCanvas.humData.shift();
                    }

                    // Перерисовываем график
                    chartCanvas.requestPaint();
                }
            }
        }
    }

    // Диалог ошибок
    Dialog {
        id: errorDialog
        title: "Ошибка"
        standardButtons: Dialog.Ok

        function show(message) {
            errorText.text = message;
            open();
        }

        Label {
            id: errorText
            anchors.fill: parent
            wrapMode: Text.WordWrap
        }
    }
}
