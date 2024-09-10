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
