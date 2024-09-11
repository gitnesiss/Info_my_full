# Проверка на вхождение значения в список
cars = ['toyota', 'audi', 'li', 'lada']
print('li' in cars)
print('bmw' in cars)

# Проверка на не вхождение значения в список
banned_users = ['andrew', 'carolina', 'ulia']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, вы можете публиковать ответы, если хотите.")
