# Перебор числовой последовательности
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Прерывание цикла while
prompt = "\nСкажи мне что-нибудь, и я повторю за тобой: "
prompt += "\nВведите 'quit' чтобы завершить программу. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Прерывание цикла из-за изменения флага
prompt = "\nСкажи мне что-нибудь, и я повторю за тобой: "
prompt += "\nВведите 'quit' чтобы завершить программу. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Прерывание цикла по команде break
prompt = "\nВведите название города, который вы посещалм: "
prompt += "\n(Введите 'quit' когда решите закончить.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("Мне понравился " + city.title() + "!")

# Продожение цикла без выполнения условий по команде continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
