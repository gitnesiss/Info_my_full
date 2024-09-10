# Если машина bmw, то вывести её название в верхнем 
# регистре, остальное с заглавной буквы.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Проверка условия равно
car_m = 'dodge'
print(car_m == 'dodgeg')