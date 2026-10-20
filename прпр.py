
import os
import sys
import platform


def main():
    results = []

    while True:
        print("\n===== ДИАГНОСТИКА СИСТЕМЫ =====")
        print("1. Имя операционной системы")
        print("2. Версия Python")
        print("3. Текущая рабочая папка")
        print("4. Список файлов в папке")
        print("5. Путь к Python")
        print("6. Архитектура системы")
        print("7. Показать все сохранённые результаты")
        print("8. Показать результат по индексу")
        print("0. Выход")

        sys.stdout.write("Выберите пункт: ")
        choice = sys.stdin.readline().strip()

        if choice == "1":
            result = platform.system()
            results.append(result)
            sys.stdout.write(f"Операционная система: {result}\n")

        elif choice == "2":
            result = sys.version
            results.append(result)
            sys.stdout.write(f"Версия Python: {result}\n")

        elif choice == "3":
            result = os.getcwd()
            results.append(result)
            sys.stdout.write(f"Текущая папка: {result}\n")

        elif choice == "4":
            result = os.listdir()
            results.append(result)
            sys.stdout.write(f"Файлы в папке: {result}\n")

        elif choice == "5":
            result = sys.executable
            results.append(result)
            sys.stdout.write(f"Путь к Python: {result}\n")

        elif choice == "6":
            result = platform.architecture()
            results.append(result)
            sys.stdout.write(f"Архитектура системы: {result}\n")

        elif choice == "7":
            if results:
                for index, value in enumerate(results):
                    sys.stdout.write(f"{index}: {value}\n")
            else:
                sys.stdout.write("Сохранённых результатов пока нет.\n")

        elif choice == "8":
            if not results:
                sys.stdout.write("Список результатов пуст.\n")
                continue

            sys.stdout.write("Введите индекс результата: ")
            index_text = sys.stdin.readline().strip()

            try:
                index = int(index_text)
                sys.stdout.write(f"Результат [{index}]: {results[index]}\n")
            except ValueError:
                sys.stdout.write("Введите целое число.\n")
            except IndexError:
                sys.stdout.write("Такого индекса нет в списке.\n")

        elif choice == "0":
            sys.stdout.write("Программа завершена.\n")
            break

        else:
            sys.stdout.write("Неверный пункт меню. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
