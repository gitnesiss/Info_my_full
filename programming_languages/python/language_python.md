[На главную страницу](../../README.md)

[На страницу выбор языков программирования](../README.md)

---

# Языки программирования Python

# Содержание

## Установка Python и его библиотек

- [Установка Python и его библиотек](language_python_lib.md)

1 [Первый файл и его запуск](#1-первый-файл-и-его-запуск)
2 [Переменные в Python. Работа со строками. Математические операции](#2-переменные-в-python-работа-со-строками-математические-операции)
3 [Списки](#3-списки)
4 [Циклы и работа со списками](#4-циклы-и-работа-со-списками)
5 [Условия if, if-else, if-elif-else.](#5-условия-if)
6 [Словари](#6-словари-и-как-с-ними-работать)

**[Исходное руководство по стилю PEP8](https://peps.python.org/pep-0008/).**

**Как установить Python и различные для него библиотек можно посмотреть по этой [ссылке](language_python_lib.md).**



# 1 Первый файл и его запуск

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

## 2 Переменные в Python. Работа со строками. Математические операции

Переменные в Python пишутся следующим образом:

```
a = 0

x, y, z = 0, 0, 0

# Константа, записывается в верхнем регистре. При этом в Python, констант не существует, поэтому эту переменную можно изменить случайно.
MAX_CONNEXTION = 5000

name = "Vasiliy Petrov"
print(name)

firstName = "vasiliy"
lastName = "petrov"
fullName = f"{firstName} {lastName}"
print(fullName)
```

`f"{firstName} {lastName}"` - называется *f-строка*. Она позволяет вставлять строковые переменные в строку.

## Методы для работы с текстом

### Изменение регистра букв

```
name = "Vasiliy Petrov"

# Первые буквы каждого слова будут с большой буквы
print(name.title())

# Все буквы слова будут выведены с большой буквы
print(name.upper())

# Все буквы слова будут выведены с маленькой буквы
print(name.lower())
```
Метод lower() особенно полезен для того, чтобы хранить данные в одинаковом формате `lower()`.

### Удаление лишних пробелов

Метод `strip()` позволяет удалять лишние пробелы если они есть в конце и в начале строки.
```
withSpaceDouble = " python "
print(f"Language {withSpaceDouble} very simple!")
print(f"Language {withSpaceDouble.rstrip()} very simple!")
print(f"Language {withSpaceDouble.lstrip()} very simple!")
print(f"Language {withSpaceDouble.strip()} very simple!")
```

## Математические операции в Python:

```
# Сложение:
print(3 + 5)  # 8

# Вычитание:
print(3 - 5)  # -2

# Умножение:
print(3 * 5)  # 15

# Деление:
print(3 / 5)  # 0,6

# Деление целых чисел всё-равно приводит к тому, что ответ получается вещественным числом:
print(4 / 2)  # 2,0

# Возведение в степень:
print(3 ** 5)  # 243

# При мат. операциях с вещественными числами ответ может немного не соответствовать ожиданиям:
print(0.2 + 0.1)  # 0.30000000000000004
```

# 3 Списки

Списки позволяют хранить в одном месте взаимосвязанные данные, сколько бы их ни было - несколько элементов или несколько миллионов элементов. Список представляет собой упорядоченный набо элементов, следующих в определённом порядке. В списке можно хранить буквы алфавита, цифры от 0 до 9 или всех работников. **Желательно присваивать спискам имена во множественном числе**: `letters`, `digits`, `names` и т.д.

В Python список обозначается квадратными скобками `[]`, а отдельные элементы списка разделяются запятыми.

```
# Базовый список:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Обращение к элементу списка по номеру
print(bicycles[1])
print(bicycles[2].title())

# Обращение к элементу списка:
print(bicycles[2])  # redline

# Обращение к последнему элементу списка:
print(bicycles[-1])  # specialized

# Изменить значение внутри списка:
bicycles[2] = "bronto"
print(bicycles)

# Использование элемента списка в формировании строки
print(f"Мой первый велосипед назывался {bicycles[0].title()}")
```

Только нужно помнить, что по правилам языка Python номер элемента в списке начинается с 0-ой позиции, а не 1-ой.

### Методы списка

#### Добавление, вставка и удаление элементов. Определение размера списка

```
# Создание пустого списка
motocycles = []
print(motocycles)

# Добавление элемента в конец списка
motocycles.append('honda')
motocycles.append('suzuki')
motocycles.append('yamaha')
motocycles.append('ural')
motocycles.append('harley')
print(motocycles)

# Добавить элемент в определённую позицию списка
motocycles.insert(2, 'ducati')
print(motocycles)

# Удалить элемент из списка
del motocycles[3]  # del yamaha
del motocycles[1]  # del suzuki
print(motocycles)

# Удалить элемент по первому вхождению
too_expensive = 'ducati'
motocycles.remove(too_expensive)  # удаляем элемент по первому вхождению
print(motocycles)
print(f"\n{too_expensive.title()} слишком дорогой для меня.")

# Определение длины списка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Длина списка cars {len(cars)}.")
```

`append()` добавляет элемент в конец спика.

При работе с методом `insert()`, при вставке элемента выходящего за пределы текущего списка, Python просто вставит этот элемент в последнюю позицию (если список длинной 5 элементов и пользователь случайно попытается вставить в позицию 8, то метод `insert()` простит ему эту ошибку и вставит элемент на 6 позицию).

Метод `remove()` отличается от `del` тем, что удаляет по содержимому в элементе. Уаляется элемент который имеет первое вхождение. Остальные элементы с таким содержимым не удалятся.  

#### Упорядочение списка

Список можно упорядочить с помощью метода `sort()`.

```
# Сортировка списка навсегда - упорядочивание по алфавиту
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Сортировка списка навсегда - упорядочивание в обратном алфавитном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(f"{cars}\n")

# Сортировка списка временная - упорядочивание по алфавиту
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(f"{cars}\n")

# Сортировка списка временная - упорядочивание в обратном алфавитном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))
print(cars)

# Вывод списка в обратном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # Переворачиваем список
print(cars)
```

Метод `reverse()` переворачивает список навсегда, но если нужно вернуть всё обратно, то можно просто воспользоваться этим метом ещё раз.

#### Методы для работы с числовыми списками

```
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Определение минимального значения в списке
print(min(digits))  # 0

# Определение максимального значения в списке
print(max(digits)) # 9

# Определение суммы всех элементов списка
print(sum(digits))  # 45
```

# 4 Циклы и работа со списками

Для перебора элементов любых списков и массивов нужно использовать циклы

```
# Цикл for для перебора каждого элемента списка и вывода его в терминал
friends = ['tolya', 'kolya', 'dima', 'serega']
for friend in friends:
    print(friend.title())
```

Для быстрого создания диапазона чисел можно использовать функцию `range()`

```
# Функция range() для построения числовых последовательностей
for value in range(1,5):
    print(value)

# Функция range() по умолчанию начинает отсчёт с числа 0
for value in range(5):
    print(value)

# Преобразуем в числовой список range() благодаря функции list()
numbers = list(range(6))  # [0, 1, 2, 3, 4, 5]
print(numbers)

# Создаёт список от 2 до 10 с шагом 2
# При этом последнее число списка обязательно меньше верхнего заданного предела.
# Если же число больше или равно, то оно откидывается.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Вывод диапазона чисел от 1 до 10 возведённых в квадрат
# и записанных в список
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
```

#### Генератор списка

В Python существует такая форма записи при создании списка со значениями как *генератор списка*:

```
# Генератор списка - создание списка со значениями в одну строку
squares = [value**2 for value in range(1, 11)]
print(squares)
```

#### Работа с частью списка - сегментами (slice)

```
players = ['Valentina', 'Xenomorf', 'Rudolf', 'Artur', 'Ken', 'Boris']
print("Базовый список:")
print(players[:])

# Вывод сегмента списка
print(players[1:3])

# Создание сегмента от начала списка
print(players[:3])

# Создание сегмента до конца списка
print(players[2:])

# Создание сегмента состоящего из 3 последних элементов списка
print(players[-3:])

# Создание сегмента из элементов списка, проская 3 элемента
print(players[::3])

# Вывод перых трёх игроков с помощью цикла for
print("\nПервые три игрока моей команды:")
for player in players[:3]:
    print(player)
```

#### Копирование элементов списка в новый список

```
my_foods = ['pizza', 'falafel', 'carrot']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
```

### Кортежи

В языке Python значения, которые не могут изменяться, называются *неизменяемыми* (immutable), а неизменяемый список называется *кортежем*.
Значения в кортеже являются неизменеямыми. При эедании изменить значение элемента кортежа, программа выдаст ошибку.

```
# Создание кортежа, определяется круглыми скобками
dimentions = (200, 50)
print(dimentions[0])
print(dimentions[1])

# Создание кортежа из одного элемента
my_kort = (3,)
print(my_kort[0])

# Перебор всех значений кортежа
for dimention in dimentions:
    print(dimention)
```

В кортеже нельзя изменить значения, но можно переопределить весь кортеж - присвоить новое значение переменной, в которой хранится кортеж.

```
# Замена размеров в кортеже путём замены самого кортежа
dimentions = (200, 50)
print("Оригинальные размеры:")
for dimention in dimentions:
    print(dimention)

dimentions = (400, 150)
print("\nИзменённые размеры:")
for dimention in dimentions:
    print(dimention)
```

# 5 Условия if

Проверка условия в Python осуществляется с учётом регистра. **Audi != audi**.

```
# Если машина bmw, то вывести её название в верхнем 
# регистре, остальное с заглавной буквы.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print()

# Проверка условия равно
car_m = 'dodge'
print(car_m == 'dodgeg')

print()

# Проверка на условия >, >=, <, <=
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
```

Проверка нескольких условий может быть осуществлена с помощью логических выражений `and` или `or`. Это аналоги Сишных && или ||. 

```
# Проверка нескольких условий and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 22
print(age_0 >= 21 and age_1 >=21)

# Проверка нескольких условий or
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >=21)
age_1 = 22
print(age_0 >= 21 or age_1 >=21)
```

```
# Проверка на вхождение значения в список
cars = ['toyota', 'audi', 'li', 'lada']
print('li' in cars)
print('bmw' in cars)

# Проверка на не вхождение значения в список
banned_users = ['andrew', 'carolina', 'ulia']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, вы можете публиковать ответы, если хотите.")
```

#### Команды условий if, if-else, if-elif-else

```
# if
age = 19
if age >= 18:
    print("Ваш возраст позволяет вам проголосовать!")
    print("Хотите зарегистрировать своё решение?")

print()

# if-else
age = 17
if age >= 18:
    print("Ваш возраст позволяет вам проголосовать!")
    print("Хотите зарегистрировать своё решение?")
else:
    print("Простите, ваш возраст не позволяет вам проголосовать!")
    print("Вы можете отдать свой голос после достижения 18 лет.")

print()

# if-elif-else
age = 12
if age < 4:
    print("Стоимость билета составляет: 0 рублей.")
elif age < 18:
    print("Стоимость билета составляет: 100 рублей.")
else:
    print("Стоимость билета составляет: 250 рублей.")

print()

# Более правильный стиль if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 100
else:
    price = 250
print(f"Стоимость билета составляет: {price} рублей.")
```

#### Проверка наличия элементов в списке

Когда имя списка используется в условии `if`, Python возвращает `True`, если список содержит хотя бы один элемент, иначе возвращается значение `False`.

```
# Проверка наличия элементов в списке
cars_selected = [] 
if cars_selected:  # если в списке есть хоть один элемент
    for car_selected in cars_selected:
        print(f"Вы выбрали автомобиль {car_selected}.")
    print("Оформляем заявку на аренду.")
else:  # если список пуст
    print("Вы уверены что не хотите арендовать автомобиль?")
```

#### Множественные списки

```
# Множественные списки
company_cars = ['audi', 'bmw', 'honda', 'lada', 'nissan', 'suzuki', 'toyota']
available_cars = ['audi', 'bmw', 'lada', 'toyota']
for car in company_cars:
    if car in available_cars:
        if car == 'bmw':
            print(f"Автомобиль {car.upper()} доступен для аренды.")
        else:
            print(f"Автомобиль {car.title()} доступен для аренды.")
    else:
        if car == 'bmw':
            print(f"Извините, автомобиль {car.upper()} не доступен для аренды.")
        else:
            print(f"Извините, автомобиль {car.title()} не доступен для аренды.")

# Множественные списки (такая же задача что и выше,
# только написанная по другому)
company_cars = ['audi', 'bmw', 'honda', 'lada', 'nissan', 'suzuki', 'toyota']
available_cars = ['audi', 'bmw', 'lada', 'toyota']
for car in company_cars:
    if car == 'bmw':
        car_name = car.upper()
    else:
        car_name = car.title()
    if car in available_cars:
        print(f"Автомобиль {car_name} доступен для аренды.")
    else:
        print(f"Извините, автомобиль {car_name} не доступен для аренды.")
```

# 6 Словари и как с ними работать

Словарь - структура данных, представляющая собой совокупность пар "ключ - значение".
Каждый ключ связывается с некоторым значением и программа может получить значение, связанное с заданным ключом. Само значение может быть числом, строкой, списком или другим словарём.

В Python словарь заключается в фигурных скобках `{}`.

```
# Инициализация пустого словаря
auto_0 = {}
print(auto_0)

# Инициализация словаря с элементами "ключ-значение"
auto_1 = {'color': 'green', 'speed_max': 180}
print(auto_1)

# Обращение к значениям в словаре
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'red', 'points': 5}
new_points = alien_0['points']
print(f"Вы получили ещё {new_points}!")

# Добавление новых пар ключ-значение
alien_0 = {'color': 'black', 'points': 10}
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

# Изменение значений в словаре
alien_0['color'] = 'yellow'
print(alien_0)

print()

# Пример работы со словарём на усечённом примере игры нападения инопланетян
# Пришелец двигается вправо
alien_0 = {'x_pos' : 0, 'y_pos' : 0, 'color': 'green', 'speed': 'medium'}
print(f"Стартовая позиция инопланетянина: {alien_0['x_pos']}.")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"Новая позиция инопланетянина: {alien_0['x_pos']}.")

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"Новая позиция инопланетянина: {alien_0['x_pos']}.")

print()

# Удаление пары ключ-значение
print("Текущий словарь:")
print(alien_0)
del alien_0['color']
print("Словарь после удаления:")
print(alien_0)

print()

# Словарь с однотипными парами ключ-значение
favorite_prog_lang = {
    'serg' : 'python',
    'psakye' : 'ruby',
    'boris' : 'c',
    'arnold' : 'android',
    'valentin' : 'c++',
    }
language = favorite_prog_lang['valentin'].title()
print(f"Валентин предпочитает язык программирования {language}.")
```





---

[В начало документа Языки программирования](#языки-программирования)

[На страницу выбор языков программирования](../README.md)

[На главную страницу](../../README.md)