#ifndef STOPWATCH_H
#define STOPWATCH_H

#pragma once            // Защита от повторного включения

#include <QObject>      // Базовый класс Qt
#include <chrono>       // Библиотека для точного измерения времени
#include <QQmlEngine>   // Для QML_ELEMENT

class Stopwatch : public QObject
{
    Q_OBJECT        // Q_OBJECT - макрос для поддержки сигналов/слотов и свойств Qt
    QML_ELEMENT     // Регистрация класса в QML. QML_ELEMENT - позволяет использовать класс в QML.

    // Свойство для отображения времени (только чтение, уведомляет об изменении через сигнал timeChanged)
    Q_PROPERTY(QString time READ time NOTIFY timeChanged)       // Q_PROPERTY - определяет свойства, доступные в QML: time - текстовое представление времени. Сигналы timeChanged уведомляет QML об изменениях

    // Свойство, указывающее, работает ли секундомер (только чтение, уведомляет через runningChanged)
    Q_PROPERTY(bool running READ running NOTIFY runningChanged) // Q_PROPERTY - определяет свойства, доступные в QML: running - состояние секундомера. Сигналы runningChanged уведомляет QML об изменениях

public:
    // Конструктор с необязательным родительским объектом
    explicit Stopwatch(QObject *parent = nullptr);

    // Метод получения форматированного времени
    QString time() const;
    // Метод для получения состояния (работает/остановлен)
    bool running() const;

public slots:  // Слоты - методы, которые можно вызывать из QML
    // Переключает состояние (старт/стоп)
    void startStop();
    // Сбрасывает секундомер
    void reset();

signals:  // Сигналы - уведомления, которые можно отправлять в QML
    // Сигнал при изменении времени
    void timeChanged();
    // Сигнал при изменении состояния
    void runningChanged();

private:
    // Обновляет время (вызывается периодически)
    void updateTime();

    // Рассчитывает точное текущее время (включая активный интервал)
    std::chrono::milliseconds getCurrentElapsed() const;

    bool m_running = false;  // Состояние: запущен или остановлен


    std::chrono::steady_clock::time_point m_startTime;  // Время последнего старта

    // Накопленное время (при паузе)
    std::chrono::milliseconds m_elapsed = std::chrono::milliseconds(0);  // Накопленное время

};

#endif // STOPWATCH_H
