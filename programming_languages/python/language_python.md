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

6 [Словари map(), множества set() и как с ними работать](#6-словари-map-множества-set-и-как-с-ними-работать)

7 [Ввод данных и цикл while](#7-ввод-данных-и-цикл-while)

8 [Функции](#8-функции)

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

# Оператор вычисления остатка отделения
print(5 % 2)  # 1
print(10 % 4)  # 2
print(3 % 3)  # 0
print(3 % 6)  # 3
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

# 6 Словари map(), множества set() и как с ними работать

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

#### Метод get() для обращения к значениям словаря

При попытке получения значения через несуществующий ключ вызовет ошибку. Чтобы этого избежать стоит использовать метод `get()`. Если ключ существует, то будет получено соответствующее значение, а если нет - будет получено значение по умолчанию `None` или информация подаваемая вторым аргументом в метод `get()`. Метод `get` может иметь однин арумент или два.

```
# Получение значения словаря по несуществующему
# Этот код выдаёт ошибку потому закоменчен
# alien_0 = {'color' : 'green', 'speed' : 'slow'}
# print(alien_0['points'])

# Получение значения словаря по несуществующему
# ключу с помощью метода get() с одним аргументом
alien_0 = {'color' : 'green', 'speed' : 'slow'}
print(alien_0.get('points'))  # None

print()

# Получение значения словаря по несуществующему
# ключу с помощью метода get(), с двумя аргументами
alien_0 = {'color' : 'green', 'speed' : 'slow'}
print(alien_0.get('points', 'Ключа points в словаре нет.'))  # None
```

#### Перебор всех пар ключ-значение, всех ключей, всех значений в словаре.

Перебор всех пар "ключ-значение" `items()` хорошо подходит для задач, где в словаре хранится один вид информации со многими разными ключами.

Когда не нужно работать со значениями в словаре, проще воспользоваться перебором только ключей, то лучше использовать метод `keys()`. Если не ипользовать метод `keys()` результат будет тем же, но читаемость кода будет по ниже.

С помощью функции `sorted()` список можно сначала отсортировать.

Метод `values()` позволяет получить значения без ключей.

Функция `set()` (множество) позволяет находить уникальные элементы списка, в результате получается не содержащий дубликатов список.
Множество оборачивается как и словарь с фигурные скобки `{}`, но при этом не имеет пары "ключ-значение", а записываются только значения через запятую.

```
# Перебор всех пар "ключ-значение"
# Словарь для пользователя сайта
user_0 = {
    'username' : 'edinorog',
    'first' : 'egor',
    'last' : 'fedotov',
    }
for key, value in user_0.items():
    print(f"\nКлюч: {key}")
    print(f"Значение: {value}")

print()

# Перебор всех ключей в словаре методом keys()
favotite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phill' : 'python',
    'boris' : 'c++',
    }
for name in favotite_languages.keys():
    print(name.title())
if 'erin' not in favotite_languages.keys():
    print("Эрин, пожалуйста пройди опрос.")

print()

# Перебор ключей словаря в определённом порядке
# Используется функция сортировки sorted()
for name in sorted(favotite_languages.keys()):
    print(f"{name.title()}, спасибо за то что проголосовал!")

print()

# Получение всех значений без ключей методом values()
favotite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phill' : 'python',
    'boris' : 'c++',
    'nastya' : 'python',
    'kostya' : 'ruby',
    }
print("Следующие языки были озвучены в опросе (с повторениями):")
for language in favotite_languages.values():
    print(language.title())
print()
# Убрать повторяющиеся значения можно с помощью функции множества set()
print("Следующие языки были озвучены в опросе (без повторений):")
for language in set(favotite_languages.values()):
    print(language.title())

print()

# Простое множество
languages = {'c++', 'ruby', 'python', 'c'}
print(f"Множество (set): {languages}")
```

#### Вложение

**Вложение** - создание сложных структур состоящих из разного набора словарей и списков. Например, можно вложить множество словарей в список, список элементов в словарь или словарь внутрь другого словаря.

Функция `range()` возвращает множество чисел.

```
# Создание списка из 3-ёх словарей
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print()

# Создание списка из 30 пришельцев (словарей)
aliens = []
# Создание 30 пришельцев
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
# Изменение атрбутов некоторых пришельцев
for alien in aliens[0:10:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
for alien in aliens[0:10:2]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'max'
# Вывод первых 12-и пришельцев
print(f"Список атрибутов пришельцев:")        
for alien in aliens[:12]:
    print(alien)
print("...")
# Вывод количества созданных пришельцев
print(f"Всего число пришельцев: {len(aliens)}")

print()

# Создание словаря со списком в качестве значения к ключу
# Сохранение информации о заказанной пицце
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra chees'],
    }
# Описание заказа
print(f"Вы заказали {pizza['crust']} - crust pizza "
    "со следующими добавками:")
for topping in pizza['toppings']:
    print("\t" + topping)

print()

# Создание словаря со списком в качестве значения к ключу
favotite_languages = {
    'jen' : ['python', 'c++'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phill' : ['python', 'android'],
    'boris' : ['c++', 'go'],
    }
for name, languages in sorted(favotite_languages.items()):
    if len(languages) == 1:
        print(f"\nУ {name.title()} в приоритете язык:")
    else:
        print(f"\nУ {name.title()} в приоритете языки:")
    for language in languages:
        print(f"\t{language.title()}")

print()

# Словарь в словаре на примеры программы с большим числом пользователей
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstain',
        'location' : 'london',
        },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

# 7 Ввод данных и цикл while

#### Ввод данных

Ввод данных в Python осуществляется с помощью функции `input()`. Эта функция воспринимает в качестве аргумента информацию, котороую вы просите пользователя выполнить для ввода.

```
# Ввод данных и подсказка что делать для ввода
name = input("Пожалуйста введите своё имя: ")
print(f"Привет, {name.title()}!")

print()

# Вынесение подсказки
prompt = "Программа сама может написать имя с заглавной буквы."
prompt += "\nВведите своё имя: "
name = input(prompt)
print(f"Привет, {name.title()}!")
```

Функция `input()` определяет всё что в неё попадает как *строки*. А бывает что нужно ввести числа, и для этого просто нужно воспользоваться функцией `int()`, которая преобразует число в виде текста в целочисленное число.

```
# Числовой ввод
prompt = "Сколько тебе лет?"
prompt += "\nВведите свой возраст: "
age = input(prompt)
print(f"Вам {int(age)} лет.")
age = int(age)
if age >= 16:
    print("Вы можете кататься на этом атракционе.")
else:
    print("Вы запрещено кататься на этом атракционе.")

print()

# Оператор вычисления остатка
number = input("Введите число, а я подскажу чётное оно или нет: ")
number = int(number)
if number % 2 == 0:
    print(f"\nЧисло {number} чётное.")
else:
    print(f"\nЧисло {number} нечётное.")
```

#### Циклы while

Цикл `while` продолжает бесконечно выполнять программу пока истинно некоторое условие.

```
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Прерывание цикла while
prompt = "\nСкажи мне что-нибудь, и я повторю за тобой: "
prompt += "\nВведите 'quit' чтобы завершить программу. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

Завершение программ может произойти по разным причинам: в игре закончилось отведённое время или закончились жизни, пользователь нажал определённую клавишу или ввёл команду на завершение программы. Программа по одному из этих условий должна завершиться. Можно завести единственную переменную - **флаг**. Эта переменная сообщает, должна ли программа выполняться далее.

```
# Перебор числовой последовательности
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Прерывание цикла while
prompt = "\nСкажи мне что-нибудь, и я повторю за тобой: "
prompt += "\nВведите 'quit' чтобы завершить программу. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Прерывание цикла из-за изменения флага
prompt = "\nСкажи мне что-нибудь, и я повторю за тобой: "
prompt += "\nВведите 'quit' чтобы завершить программу. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Прерывание цикла по команде break
prompt = "\nВведите название города, который вы посещалм: "
prompt += "\n(Введите 'quit' когда решите закончить.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("Мне понравился " + city.title() + "!")

# Продожение цикла без выполнения условий по команде continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

#### Использование цикла while со списками

Использование циклов `while` со списками и словарями позволяет собирать, хранить и упорядочивать большие объёмы данных для  последующего анализа.

Функция `pop()` извлекает из конца списка элемент для обработки.

```
# Перемещение элементов между списками
# Начинаем со списков: непроверенных пользователей и проверенных
unconfirmed_users = ['alice', 'beian', 'candace']
confirmed_users = []
# Проверяем пользователя и перемещаем в список проверенных
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Проверяем пользователя: {current_user.title()}")
    confirmed_users.append(current_user)
# Вывод списка с проверенными польхователями
print("\nСледующие пользователи были проверены:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print()

# Удаление всех вхождений конкретного значения из списка
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

```
# Опрос пользователей какие горы они хотят посетить
# Тут происходит ввод информации и запись её в словарь
responses = {}
polling_active = True

while polling_active:
    name = input("\nВведите своё имя: ")
    response = input("Какие горы ты хочешь посетить? ")
    responses[name] = response

    repeat = input("Хотите продожить опрос другим человеком? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Резульаты опроса ---")
for name, response in responses.items():
    print(f"{name.title()} хочет посетить {response.title()}.")
```

# 8 Функции

**Функции** - именнованные блоки кода, предназначенные для решения одной конкретной задачи.
**Модули** - это отдельные файлы, в которых хранятся функции для упорядочения файлов основной программы.

```
# Создание простой функции и её вывод
def greet_user():
    """Выводит простое приветствие."""  # Строка документации
    print("Привет!")

greet_user()
```

У функции есть:
**параметр** - условные данные, необходимые функции для выполнения её работы.
**аргумент** - конкретная информация, переданная при вызове функции.

```
# Создание простой функции и её вывод
def greet_user():
    """Выводит простое приветствие."""  # Строка документации
    print("Привет!")

greet_user()

print()

# Создание функции с передачей ей параметра
def greet_user_1(username):  # используется параметр
    """Выводит простое приветствие."""  # Строка документации
    print(f"Привет, {username.title()}!")

greet_user_1('василий')  # передаётся аргумент

print()

# Позиционные аргументы
def describe_pet(animal_tipe, pet_name):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet('хомяк', 'гарри')
describe_pet('кот', 'барсик')

print()

# Именнованные аргументы - можно не заботиться о позиции аргументов
def describe_pet(animal_tipe, pet_name):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet(animal_tipe = 'хомяк', pet_name = 'гарри')
describe_pet(pet_name = 'барсик', animal_tipe = 'кот')

print()

# Параметры по умолчанию, помещаются после параметров без значений
def describe_pet(pet_name, animal_tipe = 'собака'):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet('Шарик')  # не указан вид животного, но он определяется по умолчанию
describe_pet(animal_tipe = 'хомяк', pet_name = 'гарри')
describe_pet(pet_name = 'барсик', animal_tipe = 'кот')
```

#### Возвращаемое значение

```
# Возвращение простого значения из функции
def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('джимми', 'хендрикс')
print(musician)
```

#### Необязательные аргументы

Необязательные аргументы нужны когда один или несколько из аргументов могут отсутствовать. Соотвтетственно этим параметром нужно назначить в качестве параметра пустую строку со значение по умолчанию и переместить её в конец списка параметров.

```
# Необязательные аргументы
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('джимми', 'хендрикс')
print(musician)
musician = get_formatted_name('джон', 'коккер', 'ли')
print(musician)
```




---

[В начало документа Языки программирования](#языки-программирования)

[На страницу выбор языков программирования](../README.md)

[На главную страницу](../../README.md)