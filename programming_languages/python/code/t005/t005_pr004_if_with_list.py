# Применеие условия в списках:
cars_for_rent = ['audi', 'bmw', 'honda', 'lada']
for car_rent in cars_for_rent:
    if car_rent == 'bmw':
        print(f"Извините, автомобиль марки {car_rent} не доступен для аренды.")
    else:
        print(f"Автомобиль марки {car_rent} вы можете взять в аренду.")
print("Ждём вашего решения.")

print()

# Проверка наличия элементов в списке
cars_selected = [] 
if cars_selected:  # если в списке есть хоть один элемент
    for car_selected in cars_selected:
        print(f"Вы выбрали автомобиль {car_selected}.")
    print("Оформляем заявку на аренду.")
else:  # если список пуст
    print("Вы уверены что не хотите арендовать автомобиль?")

print()

# Множественные списки
company_cars = ['audi', 'bmw', 'honda', 'lada', 'nissan', 'suzuki', 'toyota']
available_cars = ['audi', 'bmw', 'lada', 'toyota']
for car in company_cars:
    if car in available_cars:
        if car == 'bmw':
            print(f"Автомобиль {car.upper()} доступен для аренды.")
        else:
            print(f"Автомобиль {car.title()} доступен для аренды.")
    else:
        if car == 'bmw':
            print(f"Извините, автомобиль {car.upper()} не доступен для аренды.")
        else:
            print(f"Извините, автомобиль {car.title()} не доступен для аренды.")

# Множественные списки
company_cars = ['audi', 'bmw', 'honda', 'lada', 'nissan', 'suzuki', 'toyota']
available_cars = ['audi', 'bmw', 'lada', 'toyota']
for car in company_cars:
    if car == 'bmw':
        car_name = car.upper()
    else:
        car_name = car.title()
    if car in available_cars:
        print(f"Автомобиль {car_name} доступен для аренды.")
    else:
        print(f"Извините, автомобиль {car_name} не доступен для аренды.")