# Ввод данных и подсказка что делать для ввода
name = input("Пожалуйста введите своё имя: ")
print(f"Привет, {name.title()}!")

print()

# Вынесение подсказки
prompt = "Программа сама может написать имя с заглавной буквы."
prompt += "\nВведите своё имя: "
name = input(prompt)
print(f"Привет, {name.title()}!")

print()

# Числовой ввод
prompt = "Сколько тебе лет?"
prompt += "\nВведите свой возраст: "
age = input(prompt)
print(f"Вам {int(age)} лет.")
age = int(age)
if age >= 16:
    print("Вы можете кататься на этом атракционе.")
else:
    print("Вы запрещено кататься на этом атракционе.")

print()

# Оператор вычисления остатка
number = input("Введите число, а я подскажу чётное оно или нет: ")
number = int(number)
if number % 2 == 0:
    print(f"\nЧисло {number} чётное.")
else:
    print(f"\nЧисло {number} нечётное.")