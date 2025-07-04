#include "Stopwatch.h"
#include <QTimer>  // Для периодического обновления
#include <QDebug>

// Конструктор: Создает таймер для обновления интерфейса
Stopwatch::Stopwatch(QObject *parent) : QObject(parent)
{
    // Таймер для обновления времени (60 раз в секунду)
    QTimer *timer = new QTimer(this);
    // Соединяем сигнал таймера timeout с нашим слотом updateTime
    connect(timer, &QTimer::timeout, this, &Stopwatch::updateTime);
    // Запускаем таймер
    timer->start(17);  // ≈60 FPS

    qInfo() << "Application started";
    qDebug() << "QML engine initialized";
}

// Рассчитывает точное текущее время (включая активный интервал)
std::chrono::milliseconds Stopwatch::getCurrentElapsed() const
{
    if (m_running) {
        // Время = накопленное + (текущее - время старта)
        return m_elapsed + std::chrono::duration_cast<std::chrono::milliseconds>(
                   std::chrono::steady_clock::now() - m_startTime);
    }

    // Если остановлен, возвращаем накопленное
    return m_elapsed;
}

// Возвращает актуальное время в любой момент, форматируя время в строку формата HH:MM:SS:zzz. time() возвращает актуальное значение через getCurrentElapsed()
QString Stopwatch::time() const
{
    // Определяем общее время в миллисекундах
    auto totalMs = getCurrentElapsed().count();

    int hours = totalMs / 3600000;
    int minutes = (totalMs % 3600000) / 60000;
    int seconds = (totalMs % 60000) / 1000;
    int ms = totalMs % 1000;

    return QString("%1:%2:%3:%4")
        .arg(hours, 2, 10, QLatin1Char('0'))  // Часы, 2 цифры, количество значений в одном разряде, заполняем нулями
        .arg(minutes, 2, 10, QLatin1Char('0'))
        .arg(seconds, 2, 10, QLatin1Char('0'))
        .arg(ms, 3, 10, QLatin1Char('0'));  // милисекунды, 3 цифры, количество значений в одном разряде, заполняем нулями
}

// Получение состояния работы
bool Stopwatch::running() const
{
    return m_running;
}

// Переключает состояние секундомера
void Stopwatch::startStop()
{
    if (m_running) {
        // Если секундомер работал, то останавливаем: сохраняем текущее накопленное время
        m_elapsed = getCurrentElapsed();
    } else {
        // Если был остановлен, то запускаем: запоминаем текущее время как время старта
        m_startTime = std::chrono::steady_clock::now();
    }

    m_running = !m_running;  // Меняем состояние

    // Отправляем сигналы об изменении состояния и времени
    emit runningChanged();
    emit timeChanged();
}

// Сбрасывает секундомер
void Stopwatch::reset()
{
    m_elapsed = std::chrono::milliseconds(0);  // Обнуляем накопленное время
    if (m_running) {
        // Если секундомер работал, то время старта устанавливаем на текущий момент
        m_startTime = std::chrono::steady_clock::now();
    }

    // Сигнализируем об изменении времени
    emit timeChanged();
}

// Вызывается таймером, обновляет время. updateTime() генерирует timeChanged()
void Stopwatch::updateTime()
{
    if (m_running) {
        // Если секундомер работает, то отправляем сигнал, что время изменилось
        emit timeChanged();  // Посылаем сигнал, только если секундомер работает
    }
}
