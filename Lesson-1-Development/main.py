def show_menu():
   
    print("\n--- Менеджер задач ---")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выход")
    print("----------------------")

def show_tasks():
   
    if not tasks:
        print("\n[!] Список задач пуст.")
        return
    
    print("\n--- Ваши задачи ---")
    for task in tasks:
       
        print(f"[{task['id']}] {task['title']}")
    print("-------------------")

def add_task():
    """Функция для добавления новой задачи."""
    global next_id
    title = input("\nВведите название новой задачи: ").strip()
    
    if title: 
        new_task = {
            'id': next_id,
            'title': title
        }
        tasks.append(new_task)
        next_id += 1 
        print(f"[+] Задача '{title}' успешно добавлена!")
    else:
        print("[-] Ошибка: Название задачи не может быть пустым.")

def edit_task():
   
    if not tasks:
        print("\n[!] Список задач пуст. Нечего редактировать.")
        return
    
    show_tasks()
    
    try:
        task_id = int(input("\nВведите ID задачи для редактирования: "))
    except ValueError:
        print("[-] Ошибка: ID должен быть числом.")
        return

   
    for task in tasks:
        if task['id'] == task_id:
            new_title = input(f"Текущее название: '{task['title']}'. Введите новое (или оставьте пустым для отмены): ").strip()
            if new_title:
                task['title'] = new_title
                print("[+] Задача успешно обновлена!")
            else:
                print("[!] Редактирование отменено.")
            return
            
    print(f"[-] Задача с ID {task_id} не найдена.")

def delete_task():
   
    if not tasks:
        print("\n[!] Список задач пуст. Нечего удалять.")
        return
    
    show_tasks()
    
    try:
        task_id = int(input("\nВведите ID задачи для удаления: "))
    except ValueError:
        print("[-] Ошибка: ID должен быть числом.")
        return

   
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            
            deleted_title = tasks.pop(i)['title']
            print(f"[+] Задача '{deleted_title}' успешно удалена!")
            return
            
    print(f"[-] Задача с ID {task_id} не найдена.")

def main():
  
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nДо свидания! Выход из приложения.")
            break 
        else:
            print("[-] Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
