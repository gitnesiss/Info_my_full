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
print(f"{cars}\n")

# Вывод в обратном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # Переворачиваем список
print(cars)

# Определение длины списка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Длина списка cars {len(cars)}.")
