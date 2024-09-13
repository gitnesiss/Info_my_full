# Возвращение простого значения из функции
def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('джимми', 'хендрикс')
print(musician)

print()

# Необязательные аргументы
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('джимми', 'хендрикс')
print(musician)
musician = get_formatted_name('джон', 'коккер', 'ли')
print(musician)
