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

# Использование элемента списка в формировании строки
print(f"Мой первый велосипед назывался {bicycles[0].title()}")

# Изменить значение внутри списка:
bicycles[2] = "bronto"
print(bicycles)