import storage
import view
import utils

def add_task(tasks):
    title = view.get_input("Введите название задачи: ")
    if not title.strip():
        view.show_message("Название не может быть пустым.")
        return

    priority = view.get_input("Введите приоритет (высокий/средний/низкий): ")
    
    new_task = {
        "title": title,
        "priority": priority if priority else "обычный",
        "done": False
    }
    tasks.append(new_task)
    storage.save_tasks(tasks)
    view.show_message(f"Задача '{title}' добавлена!")

def edit_task(tasks):
    if not tasks:
        view.show_message("Нет задач для редактирования.")
        return
    
    view.show_tasks(tasks)
    try:
        idx = int(view.get_input("Введите номер задачи для редактирования: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = view.get_input("Введите новое название (оставьте пустым, чтобы не менять): ")
            if new_title:
                tasks[idx]['title'] = new_title
            
            new_status = view.get_input("Задача выполнена? (y/n, Enter - пропустить): ")
            if new_status.lower() in ['y', 'н', 'да']:
                tasks[idx]['done'] = True
            elif new_status.lower() in ['n', 'т', 'нет']:
                tasks[idx]['done'] = False

            storage.save_tasks(tasks)
            view.show_message("Задача обновлена.")
        else:
            view.show_message("Неверный номер задачи.")
    except ValueError:
        view.show_message("Ошибка ввода. Введите число.")

def delete_task(tasks):
    if not tasks:
        view.show_message("Нет задач для удаления.")
        return

    view.show_tasks(tasks)
    try:
        idx = int(view.get_input("Введите номер задачи для удаления: ")) - 1
        if 0 <= idx < len(tasks):
            task_name = tasks[idx]['title']
            if utils.check_confirm(f"Удалить задачу '{task_name}'? "):
                tasks.pop(idx)
                storage.save_tasks(tasks)
                view.show_message("Задача удалена.")
        else:
            view.show_message("Неверный номер задачи.")
    except ValueError:
        view.show_message("Ошибка ввода. Введите число.")