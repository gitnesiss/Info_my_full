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
