# Инициализация пустого словаря
auto_0 = {}
print(auto_0)

# Инициализация словаря с элементами "ключ-значение"
auto_1 = {'color': 'green', 'speed_max': 180}
print(auto_1)

# Обращение к значениям в словаре
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'red', 'points': 5}
new_points = alien_0['points']
print(f"Вы получили ещё {new_points}!")

# Добавление новых пар ключ-значение
alien_0 = {'color': 'black', 'points': 10}
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

# Изменение значений в словаре
alien_0['color'] = 'yellow'
print(alien_0)

print()

# Пример работы со словарём на усечённом примере игры нападения инопланетян
# Пришелец двигается вправо
alien_0 = {'x_pos' : 0, 'y_pos' : 0, 'color': 'green', 'speed': 'medium'}
print(f"Стартовая позиция инопланетянина: {alien_0['x_pos']}.")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"Новая позиция инопланетянина: {alien_0['x_pos']}.")

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"Новая позиция инопланетянина: {alien_0['x_pos']}.")

print()

# Удаление пары ключ-значение
print("Текущий словарь:")
print(alien_0)
del alien_0['color']
print("Словарь после удаления:")
print(alien_0)

print()

# Словарь с однотипными парами ключ-значение
favorite_prog_lang = {
    'serg' : 'python',
    'psakye' : 'ruby',
    'boris' : 'c',
    'arnold' : 'android',
    'valentin' : 'c++',
    }
language = favorite_prog_lang['valentin'].title()
print(f"Валентин предпочитает язык программирования {language}.")