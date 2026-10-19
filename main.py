def show_message(action, title=""):
    """Выводит сообщение о результате действия."""
    if action == "add":
        print(f"\n✅ Успех: Заметка '{title}' добавлена!")
    elif action == "edit":
        print(f"\n✏️ Успех: Заметка '{title}' отредактирована!")
    elif action == "delete":
        print(f"\n🗑️ Успех: Заметка '{title}' удалена!")
    elif action == "error":
        print("\n❌ Ошибка: Неверный ввод или действие отменено.")
    else:
        print("\nℹ️ Информация: Действие выполнено.")


def show_collection(notes):
    """Красиво выводит список заметок в консоль."""
    if not notes:
        print("\n📭 Список заметок пуст.")
        return

    print("\n" + "=" * 30)
    print("       ВАШИ ЗАМЕТКИ")
    print("=" * 30)
    
    for index, note in enumerate(notes, start=1):
        # Выводим заголовок и текст заметки
        print(f"{index}. {note['title']}")
        print(f"   Текст: {note['content']}")
        print("-" * 30)


def main():
   
    notes = []

    while True:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")

        
        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            
            
            notes.append({"title": title, "content": content})
            
            
            show_message("add", title)

       
        elif choice == "2":
            show_collection(notes)

        
        elif choice == "3":
            if not notes:
                show_collection(notes) 
                continue
                
            show_collection(notes)
            try:
                idx = int(input("Введите номер заметки для редактирования: ")) - 1
                if 0 <= idx < len(notes):
                    old_title = notes[idx]['title']
                    new_title = input(f"Новый заголовок (было '{old_title}'): ")
                    new_content = input("Новый текст: ")
                    
                    notes[idx]['title'] = new_title
                    notes[idx]['content'] = new_content
                    
                    show_message("edit", new_title)
                else:
                    show_message("error")
            except ValueError:
                show_message("error")

        
        elif choice == "4":
            if not notes:
                show_collection(notes)
                continue
                
            show_collection(notes)
            try:
                idx = int(input("Введите номер заметки для удаления: ")) - 1
                if 0 <= idx < len(notes):
                   
                    deleted_title = notes[idx]['title']
                    del notes[idx]
                    show_message("delete", deleted_title)
                else:
                    show_message("error")
            except ValueError:
                show_message("error")

       
        elif choice == "5":
            print("\nДо свидания! Программа завершена.")
            break

        
        else:
            print("\n⚠️ Такого пункта нет. Введите число от 1 до 5.")



if __name__ == "__main__":
    main()