# Минимальная требуемая версия CMake (для Qt 6)
cmake_minimum_required(VERSION 3.16)

# Название проекта и язык проекта - C++
project(Stopwatch VERSION 0.1 LANGUAGES CXX)

# Включаем автоматическую обработку для Qt (moc, rcc, uic). Избавляют от ручного запуска утилит Qt
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)  # Настройки C++
set(CMAKE_AUTOMOC ON)  # Автоматически обрабатывает Q_OBJECT. Авто-генерация moc файлов. Автоматическая обработка Qt мета-объектов
set(CMAKE_AUTORCC ON)  # Авто-обработка ресурсов (.qrc)
set(CMAKE_AUTOUIC ON)  # Авто-генерация ui файлов

# Ищет Qt 6 и обязательные компоненты: Quick (QML), Gui (графика), Qml (движок QML)
find_package(Qt6 6.5 REQUIRED COMPONENTS Quick Gui Qml)

qt_standard_project_setup(REQUIRES 6.5)

# # Создаем исполняемый файл с именем проекта (Stopwatch) и добавляем исходные файлы. Перечисление всех исходных файлов (включая заголовки при ручной регистрации типа)
qt_add_executable(appStopwatch
    main.cpp
)

# Интеграция QML (самая важная часть):
#    URI Stopwatch: Пространство имен для импорта в QML
#    RESOURCE_PREFIX: Виртуальный путь в ресурсах
#    QML_FILES: Список QML-файлов
qt_add_qml_module(appStopwatch  # qt_add_qml_module - связывает QML файлы с приложением
    URI Stopwatch
    VERSION 1.0
    QML_FILES
        Main.qml
    SOURCES
        stopwatch.h
        stopwatch.cpp
)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
set_target_properties(appStopwatch PROPERTIES
#    MACOSX_BUNDLE_GUI_IDENTIFIER com.example.appStopwatch
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE  # Скрывает консольное окно при запуске
)

# Подключаем необходимые Qt модули к нашему исполняемому файлу
target_link_libraries(appStopwatch
    PRIVATE Qt6::Quick  # Qt6::Quick - необходим для QML интерфейса
)

include(GNUInstallDirs)

# Установка приложения (опционально): определяет, куда копировать приложение после сборки
install(TARGETS appStopwatch
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
