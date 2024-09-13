# Создание простой функции и её вывод
def greet_user():
    """Выводит простое приветствие."""  # Строка документации
    print("Привет!")

greet_user()

print()

# Создание функции с передачей ей параметра
def greet_user_1(username):  # используется параметр
    """Выводит простое приветствие."""  # Строка документации
    print(f"Привет, {username.title()}!")

greet_user_1('василий')  # передаётся аргумент

print()

# Позиционные аргументы
def describe_pet(animal_tipe, pet_name):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet('хомяк', 'гарри')
describe_pet('кот', 'барсик')

print()

# Именнованные аргументы - можно не заботиться о позиции аргументов
def describe_pet(animal_tipe, pet_name):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet(animal_tipe = 'хомяк', pet_name = 'гарри')
describe_pet(pet_name = 'барсик', animal_tipe = 'кот')

print()

# Параметры по умолчанию, помещаются после параметров без значений
def describe_pet(pet_name, animal_tipe = 'собака'):
    print(f"\nУ меня есть {animal_tipe}.")
    print(f"Моего {animal_tipe}а зовут {pet_name.title()}.")

describe_pet('Шарик')  # не указан вид животного, но он определяется по умолчанию
describe_pet(animal_tipe = 'хомяк', pet_name = 'гарри')
describe_pet(pet_name = 'барсик', animal_tipe = 'кот')
