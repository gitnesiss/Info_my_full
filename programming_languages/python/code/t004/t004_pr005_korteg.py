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

print("\n\n")

# Замена размеров в кортеже путём замены самого кортежа
dimentions = (200, 50)
print("Оригинальные размеры:")
for dimention in dimentions:
    print(dimention)

dimentions = (400, 150)
print("\nИзменённые размеры:")
for dimention in dimentions:
    print(dimention)
