def show_tasks(tasks):
    if tasks:
        print("\nВаши задачи:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("\nСписок задач пуст.")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    if task in tasks:
        print(f"Задача '{task}' уже существует!")
    else:
        tasks.append(task)
        print(f"Задача '{task}' добавлена.")

def remove_task(tasks):
    if tasks:
        task = input("Введите задачу для удаления: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Задача '{task}' удалена.")
        else:
            print("Такая задача не найдена.")
    else:
        print("\nСписок задач пуст.")

tasks = []

while True:
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")
    
    choice = input("Выберите действие (1-4): ")
    
    if choice == '1':
        show_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")