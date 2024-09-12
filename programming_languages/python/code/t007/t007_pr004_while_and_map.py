# Опрос пользователей какие горы они хотят посетить
# Тут происходит ввод информации и запись её в словарь
responses = {}
polling_active = True

while polling_active:
    name = input("\nВведите своё имя: ")
    response = input("Какие горы ты хочешь посетить? ")
    responses[name] = response

    repeat = input("Хотите продожить опрос другим человеком? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Резульаты опроса ---")
for name, response in responses.items():
    print(f"{name.title()} хочет посетить {response.title()}.")
