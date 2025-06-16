tasks = []  # Создаём пустой список задач

while True:
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Очистить список")
    print("6. Выйти")

    choice = input("Выберите действие (1-6): ")

    if choice == '1':
        if tasks:
            print("\nВаши задачи:")
            for task in tasks:
                print(f"- {task}")
        else:
            print("\nСписок задач пуст.")
    
    elif choice == '2':
        task = input("Введите новую задачу:\n")
        task_lower = task.lower()  # Преобразуем задачу в нижний регистр
        tasks_lower = [t.lower() for t in tasks]  # Преобразуем все задачи в списке в нижний регистр
        
        # Замена строки расположенныой выше (на 25 строке)
        # tasks_lower = []  # Создаем пустой список для задач в нижнем регистре
        # for t in tasks:   # Проходим по каждой задаче в списке tasks
        #     tasks_lower.append(t.lower())  # Добавляем задачу в нижнем регистре в новый список
        
        if task_lower in tasks_lower:  # Проверяем, есть ли задача в списке (без учета регистра)
            print(f"Задача '{task}' уже существует!")
        else:
            tasks.append(task)
            print(f"Задача '{task}' добавлена.")
    
    elif choice == '3':
        count = 1
        for task in tasks:
            print(f"{count} - {task}")
            count = count + 1
        task_num = int(input("Введите номер выполненной задачи:\n"))
        trash_sting = tasks[task_num - 1]
        tasks.pop(task_num - 1)
        tasks.insert(task_num - 1, f"[x] {trash_sting}")
        print(f"Задача '{tasks[task_num - 1]}' отмечена как выполненная.")
    
    elif choice == '4':
        if tasks:
            task = input("Введите задачу для удаления:\n")
            if task in tasks:
                tasks.remove(task)
                print(f"Задача '{task}' удалена.")
            else:
                print("\nТакая задача не найдена.")

    elif choice == '5':
        if tasks:
            tasks.clear()
            print("Список очищен.")
        else: 
            print("\nСписок задач пуст.")

    elif choice == '6':
        print("Выход из программы.")
        break

    else:
        print("\nНеверный выбор. Попробуйте снова.")
