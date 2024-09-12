# Перебор всех пар "ключ-значение"
# Словарь для пользователя сайта
user_0 = {
    'username' : 'edinorog',
    'first' : 'egor',
    'last' : 'fedotov',
    }
for key, value in user_0.items():
    print(f"\nКлюч: {key}")
    print(f"Значение: {value}")

print()

# Перебор всех ключей в словаре методом keys()
favotite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phill' : 'python',
    'boris' : 'c++',
    }
for name in favotite_languages.keys():
    print(name.title())
if 'erin' not in favotite_languages.keys():
    print("Эрин, пожалуйста пройди опрос.")

print()

# Перебор ключей словаря в определённом порядке
# Используется функция сортировки sorted()
for name in sorted(favotite_languages.keys()):
    print(f"{name.title()}, спасибо за то что проголосовал!")

print()

# Получение всех значений без ключей методом values()
favotite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phill' : 'python',
    'boris' : 'c++',
    'nastya' : 'python',
    'kostya' : 'ruby',
    }
print("Следующие языки были озвучены в опросе (с повторениями):")
for language in favotite_languages.values():
    print(language.title())
print()
# Убрать повторяющиеся значения можно с помощью функции множества set()
print("Следующие языки были озвучены в опросе (без повторений):")
for language in set(favotite_languages.values()):
    print(language.title())

print()

# Простое множество
languages = {'c++', 'ruby', 'python', 'c'}
print(f"Множество (set): {languages}")