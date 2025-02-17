# Цикл for для перебора каждого элемента списка и вывода его в терминал
friends = ['tolya', 'kolya', 'dima', 'serega']
for friend in friends:
    print(friend.title())

# Функция range() для построения числовых последовательностей
for value in range(1,5):
    print(value)  # 1, 2, 3, 4

# Функция range() по умолчанию начинает отсчёт с числа 0
for value in range(5):
    print(value)  # 0, 1, 2, 3, 4

# Преобразуем в числовой список range() благодаря функции list()
numbers = list(range(6))  # [0, 1, 2, 3, 4, 5]
print(numbers)

# Создаёт список от 2 до 10 с шагом 2
# При этом последнее число списка обязательно меньше верхнего заданного предела, если больше или равно, то оно откидывается.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Вывод диапазона чисел от 1 до 10 возведённых в квадрат и записанных в список
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
