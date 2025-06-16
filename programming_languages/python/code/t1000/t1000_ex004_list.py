# Список
fruits = ["яблоко", "апельсин", "банан"]

# Цикл for
for fruit in fruits:
    print(fruit)

fruits.append("киви")
fruits.append("виноград")

print("\nДобавили киви и виноград:")
for fruit in fruits:
    print(fruit)

fruits.remove("банан")

print("\nУдалили банан:")
for fruit in fruits:
    print(fruit)