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
    