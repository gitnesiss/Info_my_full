# Получение значения словаря по несуществующему
# Этот код выдаёт ошибку потому закоменчен
# alien_0 = {'color' : 'green', 'speed' : 'slow'}
# print(alien_0['points'])

# Получение значения словаря по несуществующему
# ключу с помощью метода get() с одним аргументом
alien_0 = {'color' : 'green', 'speed' : 'slow'}
print(alien_0.get('points'))  # None

print()

# Получение значения словаря по несуществующему
# ключу с помощью метода get(), с двумя аргументами
alien_0 = {'color' : 'green', 'speed' : 'slow'}
print(alien_0.get('points', 'Ключа points в словаре нет.'))  # None
