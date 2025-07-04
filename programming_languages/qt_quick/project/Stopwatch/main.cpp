#include <QGuiApplication>          // Базовый класс приложения (без виджетов)
#include <QQmlApplicationEngine>    // Движок QML

int main(int argc, char *argv[])
{
    // Создаем приложение
    QGuiApplication app(argc, argv);

    // Создаем движок QML
    QQmlApplicationEngine engine;

    // Обработка ошибки загрузки QML
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreationFailed,   //  **Подключение сигнала `objectCreationFailed`**: обработчик на случай, если загрузка QML-файла не удалась. Это важно для отлова ошибок при запуске приложения.
        &app,
        []() {
            // Выход с ошибкой
            QCoreApplication::exit(-1);
        },
        Qt::QueuedConnection);

    // **Отсутствует явная регистрации типа**: Не используется `qmlRegisterType<Stopwatch>("Stopwatch", 1, 0, "Stopwatch")` для регистрации типа. В стандартном шаблоне этого нет, потому что в CMake-проекте использовалась `qt_add_qml_module`, которая автоматически регистрирует типы, если они указаны в QML_FILES как ассоциированные с C++.

    // Загружаем главный QML файл из модуля (указанного в qt_add_qml_module)
    engine.loadFromModule("Stopwatch", "Main");         // engine.loadFromModule - загружает главный QML файл

    // Запускаем цикл обработки событий
    return app.exec();
}
