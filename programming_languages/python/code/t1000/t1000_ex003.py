try:
    num1 = float(input("Введите первое число\n"))
    num2 = float(input("Введите второе число\n"))
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Неверная операция! Делить на 0 нельзя.")
            exit()
        result = num1 / num2
    else:
        print("Неверная операция!")
        exit()

    print(f"Результат: {result}")
    
except ValueError:
    print("Ошибка: вы ввели не число!")