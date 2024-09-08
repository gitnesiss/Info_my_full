[На главную страницу](../../README.md)

[На страницу выбор языков программирования](../README.md)

# Языки программирования Python

# Содержание

- [Начало работы с Python](#начало-работы-с-python)

# Начало работы с Python

## Установка Python и его библиотек

# Содержанине раздела

[Установка Python в Windows](#1-установка-python-в-windows)

[Сборка QtCreator из исходников](#2-сборка-qtcreator-из-исходников)

[Установка QT в Windows с помощью MSYS2](#3-установка-qt-в-windows-с-помощью-msys2)


# 1 Установка Python в Windows

## 1.1 Проверяем наличие Python и устанавливаем его

```
# Для Windows
python --version

# Для UNIX
python3 --version
```

Если в терминале получен похожий ответ `Python 3.11.8`, то это означает, что  Python установлен.

Если ответ похож на `Python is not defined`, то для ОС Windows скачиваем [установщик](https://www.python.org/downloads/).

```
# Устанавливаем Python на UNIX
sudo apt-get update -y
sudo apt-get install python3
```

## 1.2 Устаналвиваем PIP (предпочитаемый установщик программ) для Python и обновляем его

При версиях Python выше 3.4 `pip` должен устанавливаться с установкой самого Python. Если этого не произошло, то можно его установить с помощью

```
# Для UNIX и RaspberryPi
sudo apt-get install python3-pip
```

Обновить pip можно с помощью команд

```
# Для Windows
python -m pip install -U pip

# Для UNIX и RaspberryPi
pip install -U pip
```

### Проверка установленной версии python в системе

В терминале следует ввести 

```
# в ОС Windows
python --version

# в ОС Linux
python3 --version
```

Если в системе установлен Python, то в терминал будет выведена следующая информация (номер версии может отличаться):

```
Python 3.11.0
```

### Первый файл и его запуск

Создадим файл **hello_world.py** в нём пишем инстукции:

```
print("Hello Python world!")
```

Запустить этот файл можно двумя способами:

1. В терминале, находясь в каталоге с файлом, вводим:

```
# в ОС Windows при использовании оболочки powershell
python .\hello_world.py

# в ОС Windows при использовании оболочки bash
python hello_world.py
```

2. Используя Visual Studio Code, с установленными расширениями для языка Python, при этом активным должно быть окно с запускаемым кодом, нажать на стрелку запуска "Run Python file".

В обоих случаях в терминале будет выведена информация:

```
Hello Python world!
```

### Переменные в Python

```
name = "Vasiliy Petrov"
print(name)
```

### Форматирование текста

```
name = "Vasiliy Petrov"

# Первые буквы каждого слова будут с большой буквы
print(name.title())

# Все буквы слова будут выведены с большой буквы
print(name.upper())

# Все буквы слова будут выведены с маленькой буквы
print(name.lower())
```

Метод lower() особенно полезен для того чтобы хранить данные 

### Использование переменных в строках

```
firstName = "vasiliy"
lastName = "petrov"
fullName = f"{firstName} {lastName}"
print(fullName)
```

`f"{firstName} {lastName}"` - называется *f-строка*

---

[В начало документа Языки программирования](#языки-программирования)

[На страницу выбор языков программирования](../README.md)

[На главную страницу](../../README.md)