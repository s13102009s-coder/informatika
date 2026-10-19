import view
import core
import storage
import sys

def main():
    tasks = storage.load_tasks()
    
    while True:
        view.show_menu()
        choice = view.get_input("Выберите действие: ")

        if choice == '1':
            view.show_tasks(tasks)
        elif choice == '2':
            core.add_task(tasks)
        elif choice == '3':
            core.edit_task(tasks)
        elif choice == '4':
            core.delete_task(tasks)
        elif choice == '0':
            print("До свидания!")
            sys.exit()
        else:
            view.show_message("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()