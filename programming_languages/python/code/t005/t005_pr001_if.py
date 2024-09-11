# Если машина bmw, то вывести её название в верхнем 
# регистре, остальное с заглавной буквы.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print()

# Проверка условия равно
car_m = 'dodge'
print(car_m == 'dodgeg')

print()

# Проверка на условия >, >=, <, <=
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print()

# Проверка нескольких условий and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 22
print(age_0 >= 21 and age_1 >=21)

# Проверка нескольких условий or
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >=21)
age_1 = 22
print(age_0 >= 21 or age_1 >=21)