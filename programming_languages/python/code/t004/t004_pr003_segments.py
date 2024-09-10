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
    