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
print(motocycles)