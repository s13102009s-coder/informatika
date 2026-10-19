def show_menu():
    print("\n--- МЕНЕДЖЕР ЗАДАЧ ---")
    print("1. Показать все задачи")
    print("2. Создать задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("0. Выход")
    print("----------------------")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    
    print("\n--- Ваши задачи ---")
    for index, task in enumerate(tasks, 1):
        status = "[+]" if task.get('done') else "[ ]"
        print(f"{index}. {status} {task['title']} (Приоритет: {task.get('priority', 'обычный')})")
    print("-------------------")

def show_message(msg):
    print(f">>> {msg}")

def get_input(prompt):
    return input(prompt)